from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import requests
import datetime

app = Flask(__name__)

# กำหนดค่า JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # เปลี่ยนเป็นคีย์ของคุณ
jwt = JWTManager(app)

# ElasticSearch URL และ API Key
ES_URL = 'https://my-observability-project-e8416d.es.us-east-1.aws.elastic.cloud:443/user-logs-/_doc'
API_KEY = 'OWZUWWU1WUJRVHRTR3FKYkFua246UEtScEswdnM3dE5rMmVzbWJUZWx3dw=='

# ฟังก์ชันเพื่อส่ง log ไปที่ ElasticSearch
def send_log_to_elasticsearch(log_data):
    headers = {
        'Authorization': f'ApiKey {API_KEY}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(ES_URL, headers=headers, json=log_data)
        print(f"Sent log: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending log: {e}")

# ฟังก์ชัน login สำหรับตรวจสอบ user
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != "admin" or password != "password":  # เปลี่ยนให้ตรงกับข้อมูลจริงของคุณ
        return jsonify({"msg": "Bad username or password"}), 401

    # สร้าง JWT Token
    access_token = create_access_token(identity=username)

    # ส่ง log ไปยัง ElasticSearch
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "username": username,
        "message": "User logged in successfully"
    }
    send_log_to_elasticsearch(log_entry)

    return jsonify(access_token=access_token), 200

# ฟังก์ชันที่จำเป็นต้องมีการยืนยันตัวตน
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Welcome to the protected route!")

if __name__ == '__main__':
    app.run(debug=True)
