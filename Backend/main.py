from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from typing import List
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import  config

app = FastAPI()

# Database Connection
def get_db_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
        port=config.DB_PORT
    )

# Data Model
class FraudTransaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    location: str
    device_id: str
    timestamp: str

# API Endpoint to Fetch Fraud Transactions
@app.get("/fraud", response_model=List[FraudTransaction])
def get_fraud_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_id, user_id, amount, location, device_id, timestamp FROM transactions.fraud")
    data = cursor.fetchall()
    conn.close()

    fraud_list = []
    for row in data:
        fraud_list.append({
            "transaction_id": row[0],
            "user_id": row[1],
            "amount": row[2],
            "location": row[3],
            "device_id": row[4],
            "timestamp": row[5]
        })

    return fraud_list
