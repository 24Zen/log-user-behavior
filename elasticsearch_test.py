import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# โหลดค่าจากไฟล์ .env
load_dotenv()

# อ่านค่า ELASTIC_URL และ ELASTIC_API_KEY จาก .env
elastic_url = os.getenv("ELASTIC_URL")
elastic_api_key = os.getenv("ELASTIC_API_KEY")

# เชื่อมต่อกับ Elasticsearch
es = Elasticsearch(
    elastic_url,  # ใช้ URL จาก .env
    api_key=elastic_api_key  # ใช้ API Key จาก .env
)

# ทดสอบการเชื่อมต่อ
response = es.info()
print(response)
