from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS  # ✅ เพิ่มบรรทัดนี้
import requests
import datetime
import json

app = Flask(__name__)
CORS(app)  # ✅ เปิด CORS ทั้งหมด (หรือกำหนด origin ภายหลังได้)

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'
jwt = JWTManager(app)

# ... โค้ดเดิมทั้งหมดไม่ต้องเปลี่ยน ...

# ตั้งค่า Elasticsearch
ES_URL = ''
API_KEY = ''  # ใส่ API Key ของคุณ

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

# API สำหรับ Login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # ตรวจสอบ username และ password (ในที่นี้ใช้ hardcode แต่สามารถเชื่อมกับฐานข้อมูลได้)
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    # สร้าง JWT token
    access_token = create_access_token(identity=username)
    
    # ส่ง log เข้า ElasticSearch
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "username": username,
        "action": "login",
        "message": f"User {username} logged in"
    }
    send_log_to_elasticsearch(log_entry)
    
    return jsonify(access_token=access_token)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
