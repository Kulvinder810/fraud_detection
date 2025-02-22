# 🚀 Real-Time Data Pipeline with Kafka, Spark, and Databricks

A scalable **real-time data pipeline** using **Confluent Kafka** as a message broker, a **Python Producer** to simulate transactions, and a **Databricks Consumer** to process the data.

---

## 📂 Project Structure

```
/project-root/
│── producer/           # Python Kafka Producer
│   ├── producer.py     # Sends messages to Kafka (Confluent)
│── consumer/           # Databricks Consumer
│   ├── consumer.py     # Reads and processes messages
│── config/             # Stores configuration settings
│   ├── config.py       # User-defined settings (Kafka, Database)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .gitignore          # Ignore unnecessary files
```

---

## 🛠️ Prerequisites

Ensure you have the following installed before proceeding:

✅ **Python 3.8+**  
✅ **Kafka (Confluent Cloud or Local Setup)**  
✅ **Databricks Cluster** (For consumer processing)  
✅ **Confluent Kafka Python Library**  

---

## ⚙️ Configuration Setup

Edit the `config.py` file inside the **config/** folder to match your setup.

```python
# Confluent Kafka Configuration
KAFKA_CONFIG = {
    "bootstrap.servers": "your-confluent-bootstrap-url:9092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "your-api-key",
    "sasl.password": "your-api-secret",
}

KAFKA_TOPIC = "transactions"

🔒 **Never hardcode sensitive credentials. Use `.env` or environment variables.**  

---

## 🚀 Running the Producer (Python)

1️⃣ **Navigate to the producer folder**  
```bash
cd producer
```

2️⃣ **Install dependencies**  
```bash
pip install -r ../requirements.txt
```

3️⃣ **Run the producer**  
```bash
python producer.py
```

📌 **This script will send transaction data to Kafka every few seconds.**  

---

## 🔥 Running the Consumer (Databricks)

1️⃣ **Upload `consumer.py` to your Databricks workspace**  
2️⃣ **Attach it to a Databricks cluster**  
3️⃣ **Run the script in a notebook or as a job**  

📌 **The consumer will read Kafka messages and process them in Databricks.**  

---

## 🐛 Troubleshooting

❌ **Producer not sending messages?**  
✔️ Ensure Kafka is running:  
```bash
confluent login
confluent kafka cluster list
confluent kafka topic list
```
✔️ Verify your **Kafka topic exists**:  
```bash
confluent kafka topic describe transactions
```

❌ **Databricks not receiving messages?**  
✔️ Check if the consumer script is properly consuming from Kafka by running it manually in Databricks.


---

## 💡 Contributing

🚀 Contributions are welcome! Feel free to submit a **pull request** or open an **issue** if you find any bugs or have feature requests.

---

## 👨‍💻 Author

👤 **Kulvinder Singh**  
🔗 [GitHub Profile](https://github.com/Kulvinder810)  
✉️ Contact: kuls810@gmail.com  

---

### 🎉 **Happy Coding! 🚀🔥**
