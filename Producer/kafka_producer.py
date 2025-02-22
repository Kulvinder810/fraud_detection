from confluent_kafka import Producer
import json
import random
import time
from faker import Faker
import datetime as dt

fake = Faker()
conf={
    'bootstrap.servers':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', #the server endpoint goes here
    'security.protocol':'SASL_SSL',
    'sasl.mechanism':'PLAIN',
    'sasl.username':'XXXXXXXXXXXX',  #api key goes here
    'sasl.password':'XXXXXXXXXXXXXXX', #api key secret goes here
    'client.id':'XXXXXXXXXXX' #client id like John's pc etc 
}

KAFKA_TOPIC = "transactions"   

producer=Producer(conf)

def generate_transaction():
    return {
        "transaction_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "amount": round(random.uniform(5, 20000), 2),
        "location": fake.city(),
        "device_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
    }

def acked(err,msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        msg_key=msg.key()
        msg_value=msg.value()
        print(f"Message produced: key is {msg_key} and values is {msg_value}")

while True:
    transaction = generate_transaction()
    json_data=json.dumps(transaction)
    producer.produce(KAFKA_TOPIC,key=transaction['transaction_id'],value=json_data,callback=acked)
    print(f"Sent: {transaction}")
    time.sleep(1)  # Sending 1 transaction per second
