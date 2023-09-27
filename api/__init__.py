from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from api.routes import api
from api import db

info = Info(title='Microserviço Empresa', version='0.1.0',
            description='CRUD de Empresa')

app = OpenAPI(__name__, info=info)

# CORS(app, allow_headers='*', origins='*')
CORS(app)

app.register_api(api)
