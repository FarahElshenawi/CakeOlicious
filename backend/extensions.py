<<<<<<< HEAD
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import sys
# sys.path.append('C:/Fara7 repo/CakeOlicious/venv/Lib/site-packages')

# db = SQLAlchemy()
# migrate = Migrate()
# extensions.py
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.config.config import Config

db = SQLAlchemy()
jwt = JWTManager()


# دالة الاتصال بقاعدة البيانات
def get_db_connection():
    return db
=======
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAalchemy
db = SQLAlchemy()
>>>>>>> d1b9626457fb9e49c0350bd926779b3f4fbfd806
