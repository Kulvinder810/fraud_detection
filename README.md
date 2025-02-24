# 🚀 Real-Time Fraud Detection Dashboard

This project is a **Real-Time Fraud Detection System** that processes streaming data from **Confluent Kafka**, performs analysis using **Apache Spark on Databricks**, and visualizes the fraud patterns using a **Flask + FastAPI frontend** with interactive charts.

---

## 📌 Features

✅ **Real-time fraud detection** using Kafka and Spark  
✅ **Top-N Fraud Locations** bar chart using **Chart.js**  
✅ **Responsive UI** with Bootstrap for smooth resizing  
✅ **Dynamic Table with Pagination & Scroll**  
✅ **Backend with FastAPI + PostgreSQL (AWS RDS)**  
✅ **Dark Mode support** for a modern look  

---

## 🏗️ Project Structure

```
fraud-detection-dashboard/
│-- backend/                    # FastAPI Backend
│   ├── main.py                  # API Endpoints
│   ├── database.py               # PostgreSQL connection
│   ├── models.py                 # Database models
│   ├── schemas.py                # Data schemas
│   ├── requirements.txt          # Backend dependencies
│
│-- frontend/                   # Flask Frontend
│   ├── static/
│   │   ├── styles.css            # Custom CSS for UI
│   │   ├── script.js             # JavaScript for interactivity
│   ├── templates/
│   │   ├── index.html            # Main dashboard UI
│   ├── app.py                    # Flask server
│   ├── requirements.txt          # Frontend dependencies
│
│-- spark_jobs/                  # Apache Spark Jobs
│   ├── fraud_detection.py        # Spark processing logic
│
│-- README.md                    # Project Documentation
│-- .gitignore                    # Git ignored files
```

---

## ⚙️ Setup Guide

### **1️⃣ Backend (FastAPI)**
1. Navigate to the `backend` folder:
   ```sh
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the FastAPI backend:
   ```sh
   uvicorn main:app --reload
   ```

---

### **2️⃣ Frontend (Flask)**
1. Navigate to the `frontend` folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```sh
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

### **3️⃣ Database Setup (PostgreSQL on AWS RDS)**
1. Create an **AWS RDS PostgreSQL** instance  
2. Add inbound security rules to allow connections  
3. Update `config.py` with the correct **RDS endpoint, username, and password**  
4. Run the rds_Setup.sql script on IDE/terminal to create the fraud table:

---

### **4️⃣ Streaming Data from Kafka to Spark**
1. Start the Kafka producer to send data to the topic  
2. Run the Spark job to process the stream:
   ```sh
   spark-submit fraud_detection.py
   ```

---

## 📊 Visualization Dashboard

The frontend displays:  
📌 **Top 10 Fraud Locations Bar Chart**  
📌 **Paginated Fraud Table with Search**  
📌 **Real-time Fraud Monitoring**

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, PostgreSQL (AWS RDS)
- **Frontend:** Flask, Chart.js, Bootstrap
- **Streaming & Processing:** Confluent Kafka, Apache Spark (Databricks)
- **Database:** PostgreSQL

---

## 🤝 Contributing

1. Fork the repo  
2. Create a new branch (`feature-branch`)  
3. Commit changes & push  
4. Open a PR 🚀  

---


