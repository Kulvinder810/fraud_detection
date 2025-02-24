from flask import Flask, render_template
import requests

app = Flask(__name__)

# FastAPI Backend URL
FASTAPI_URL = "http://127.0.0.1:8000/fraud"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/fraud-data')
def fetch_fraud_data():
    try:
        response = requests.get(FASTAPI_URL)
        if response.status_code == 200:
            fraud_data = response.json()
        else:
            fraud_data = []
    except Exception as e:
        fraud_data = []
        print("Error fetching fraud data:", e)

    return {"data": fraud_data}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
