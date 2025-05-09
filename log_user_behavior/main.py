"""
from dotenv import load_dotenv
import os

# โหลดข้อมูลจาก .env
load_dotenv()

# ดึงค่า URL และ API Key จาก .env
elastic_url = os.getenv("ELASTIC_URL")
api_key = os.getenv("ELASTIC_API_KEY")

print(f"URL: {elastic_url}")
print(f"API Key: {api_key}")
"""

from flask import Flask, request
import requests
import datetime
import json

app = Flask(__name__)

# ตั้งค่า Elasticsearch
ES_URL = 'https://my-observability-project-e8416d.es.us-east-1.aws.elastic.cloud:443/user-logs-/_doc'
API_KEY = 'OWZUWWU1WUJRVHRTR3FKYkFua246UEtScEswdnM3dE5rMmVzbWJUZWx3dw=='  # ใส่ API Key ของคุณ

# ฟังก์ชันส่ง log
def send_log_to_elasticsearch(log_data):
    headers = {
        'Authorization': f'ApiKey {API_KEY}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(ES_URL, headers=headers, data=json.dumps(log_data))
        print(f"Sent log: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending log: {e}")

@app.route('/')
def index():
    log_entry = {
        "@timestamp": datetime.datetime.utcnow().isoformat(),
        "path": request.path,
        "method": request.method,
        "message": "User accessed the home page"
    }
    send_log_to_elasticsearch(log_entry)
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
