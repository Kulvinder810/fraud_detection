from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import  config

DATABASE_URL = f"postgresql://{config.DB_USER}:{config.DB_PASS}{config.DB_HOST}/{config.DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB Model
class FraudTransaction(Base):
    __tablename__ = "transactions.fraud"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, index=True)
    user_id = Column(String)
    amount = Column(Float)
    location = Column(String)
    device_id=Column(String)
    timestamp = Column(String)


app = FastAPI()

@app.get("/fraud-transactions")
def get_fraud_transactions():
    session = SessionLocal()
    transactions = session.query(FraudTransaction).all()
    session.close()
    return transactions
