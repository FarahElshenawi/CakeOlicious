# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import sys
# sys.path.append('C:/Fara7 repo/CakeOlicious/venv/Lib/site-packages')

# db = SQLAlchemy()
# migrate = Migrate()
# extensions.py
import pyodbc
from flask_jwt_extended import JWTManager
from config.config import Config

# دالة الاتصال بقاعدة البيانات
def get_db_connection():
    return pyodbc.connect(Config.SQL_CONNECTION_STRING)

# تهيئة JWT
jwt = JWTManager()