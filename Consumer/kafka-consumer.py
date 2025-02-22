from pyspark.sql.functions import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import  config

confluentBootstrapServers = config.KAFKA_SERVER
confluentApiKey = config.KAFKA_API_KEY
confluentSecret = config.KAFKA_API_SECRET
confluentTopicName = config.KAFKA_TOPIC
confluentTargetTopicName=config.KAFKA_TARGET_TOPIC

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

converted_orders_df = transaction_df.selectExpr("CAST(key as string) AS key","CAST(value as string) AS value","topic","partition","offset","timestamp","timestampType")

transaction_schema = "transaction_id string,user_id string,amount float,location string,device_id string,timestamp string"


parsed_transactions_df = converted_orders_df.select("key",from_json("value",transaction_schema).alias("value"),"topic","partition","offset","timestamp","timestampType")
parsed_transactions_df.createOrReplaceTempView("transactions")
exploded_orders = spark.sql("""select key, value.transaction_id as transaction_id, value.user_id as user_id, value.amount as amount,
          value.location as location, value.device_id as device_id, value.timestamp as timestamp  from transactions""")

exploded_orders \
.writeStream \
.queryName("ingestionquery") \
.format("delta") \
.outputMode("append") \
.option("checkpointLocation","checkpointdirtransaction302") \
.toTable("transaction_new")

filtered_orders = spark.sql("select CAST(key as string) AS key, CAST(value as string) AS value from transactions where value.amount > 1000")

filtered_orders \
.writeStream \
.queryName("streamquery") \
.format("kafka") \
.outputMode("append") \
.option("checkpointLocation","checkpointdir3044") \
.option("kafka.bootstrap.servers",confluentBootstrapServers) \
.option("kafka.security.protocol","SASL_SSL") \
.option("kafka.sasl.mechanism","PLAIN") \
.option("kafka.sasl.jaas.config", "kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username='{}' password='{}';".format(confluentApiKey, confluentSecret)) \
.option("kafka.ssl.endpoint.identification.algorithm","https") \
.option("topic",confluentTargetTopicName) \
.start()



