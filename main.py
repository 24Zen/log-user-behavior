from elasticapm import Client
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

app = Flask(__name__)

# Configure Elastic APM
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'my-flask-app',  # Change this to your service name
    'SECRET_TOKEN': 'OWZUWWU1WUJRVHRTR3FKYkFua246UEtScEswdnM3dE5rMmVzbWJUZWx3dw==',  # Your API Key
    'SERVER_URL': 'https://my-observability-project-e8416d.apm.us-east-1.aws.elastic.cloud:443',  # Your APM Server URL
}

elastic_apm = ElasticAPM(app)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
