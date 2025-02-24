from pyspark.sql.functions import col, from_json, struct, to_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import psycopg2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import  config

confluentBootstrapServers = config.KAFKA_SERVER
confluentApiKey = config.KAFKA_API_KEY
confluentSecret = config.KAFKA_API_SECRET
confluentTopicName = config.KAFKA_TOPIC


# Define schema for incoming data
schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("location", StringType(), True),
    StructField("device_id", StringType(), True),
    StructField("timestamp", StringType(), True)
])

transaction_df = spark \
.readStream \
.format("kafka") \
.option("kafka.bootstrap.servers",confluentBootstrapServers) \
.option("kafka.security.protocol","SASL_SSL") \
.option("kafka.sasl.mechanism","PLAIN") \
.option("kafka.sasl.jaas.config", "kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username='{}' password='{}';".format(confluentApiKey, confluentSecret)) \
.option("kafka.ssl.endpoint.identification.algorithm","https") \
.option("subscribe",confluentTopicName) \
.option("startingTimestamp",1) \
.option("maxOffsetsPerTrigger",50) \
.load()

# Deserialize JSON
df_parsed = transaction_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Fraud Detection Logic
df_fraud = df_parsed.filter(col("amount") > 10000)  # Example rule

# Write fraud transactions to AWS RDS
def write_to_rds(batch_df, batch_id):
    db_connection = psycopg2.connect(
        host="finaank-database.c9uqeog0amez.ap-south-1.rds.amazonaws.com",
        dbname="transactions_DB",
        user="postgres",
        password="password",
        port="5432"
    )
    cursor = db_connection.cursor()

    for row in batch_df.collect():
        cursor.execute("INSERT INTO transactions.fraud (transaction_id, user_id, amount, location, device_id, timestamp) VALUES (%s, %s, %s, %s, %s,%s)",
                       (row.transaction_id, row.user_id, row.amount, row.location, row.device_id , row.timestamp))

    db_connection.commit()
    cursor.close()
    db_connection.close()

df_fraud.writeStream.foreachBatch(write_to_rds).start().awaitTermination()