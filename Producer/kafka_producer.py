from confluent_kafka import Producer
import json
import random
import time
from faker import Faker
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import  config

fake = Faker()
conf={
    'bootstrap.servers':config.KAFKA_SERVER, #the server endpoint goes here
    'security.protocol':'SASL_SSL',
    'sasl.mechanism':'PLAIN',
    'sasl.username': config.KAFKA_API_KEY,  #api key goes here
    'sasl.password':config.KAFKA_API_SECRET, #api key secret goes here
    'client.id':'XXXXXXXXXXX' #client id like John's pc etc 
}

topic=config.KAFKA_TOPIC

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
    producer.produce(topic,key=transaction['transaction_id'],value=json_data,callback=acked)
    print(f"Sent: {transaction}")
    time.sleep(1)  # Sending 1 transaction per second
