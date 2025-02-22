📌 Real-Time Data Pipeline using Kafka, Spark, and Databricks
🚀 A scalable real-time data pipeline using Apache Kafka as a message broker, a Python Producer to simulate transactions, and a Databricks Consumer to process the data.

📂 Project Structure
bash
Copy
Edit
/project-root/
│── producer/           # Python Kafka Producer
│   ├── producer.py     # Sends messages to Kafka
│── consumer/           # Databricks Consumer
│   ├── consumer.py     # Reads and processes messages
│── config/             # Stores configuration settings
│   ├── config.py       # User-defined settings
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .gitignore          # Ignore unnecessary files
🛠️ Prerequisites
Ensure you have the following installed before proceeding:
✅ Python 3.8+
✅ Kafka & Zookeeper (Running on localhost or a cloud service)
✅ Databricks Cluster (For consumer processing)
✅ Confluent Kafka (Optional for managed Kafka)

⚙️ Configuration Setup
Edit the config.py file inside the config/ folder to match your setup.

python
Copy
Edit
# Kafka Settings
KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "transactions"

🚀 Running the Producer (Python)
1️⃣ Navigate to the producer folder

bash
Copy
Edit
cd producer
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r ../requirements.txt
3️⃣ Run the producer

bash
Copy
Edit
python producer.py
📌 This script will send transaction data to Kafka every few seconds.

🔥 Running the Consumer (Databricks)
1️⃣ Upload consumer.py to your Databricks workspace
2️⃣ Attach it to a Databricks cluster
3️⃣ Run the script in a notebook or as a job

📌 The consumer will read Kafka messages and process them in Databricks.

📈 Monitoring Kafka Topics
To check if data is flowing correctly, run the following command:

bash
Copy
Edit
kafka-console-consumer --bootstrap-server localhost:9092 --topic transactions --from-beginning
🐛 Troubleshooting
❌ Producer not sending messages?
✔️ Ensure Kafka is running:

bash
Copy
Edit
zookeeper-server-start.sh config/zookeeper.properties  
kafka-server-start.sh config/server.properties  
✔️ Verify your Kafka topic exists:

bash
Copy
Edit
kafka-topics --list --bootstrap-server localhost:9092
❌ Databricks not receiving messages?
✔️ Check if the consumer script is properly consuming from Kafka by running it manually in Databricks.


💡 Contributing
🚀 Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have feature requests.

👨‍💻 Author
👤 Kulvinder Singh
🔗 github.com/Kulvinder810/
✉️ Contact: kuls810@gmail.com

🎉 Happy Coding! 🚀🔥
Let me know if you need any modifications or improvements! 🚀







