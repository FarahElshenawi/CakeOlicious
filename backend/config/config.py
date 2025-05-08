<<<<<<< HEAD
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     DRIVER = os.environ.get('DRIVER')
#     SERVER = os.environ.get('SERVER')
#     DATABASE = os.environ.get('DATABASE')
#     DRIVER = DRIVER.replace(' ', '+')
#     SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# config/config.py
import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-here")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///cakeolicious.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key-here")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


# import secrets
# print(secrets.token_hex(32))
=======
import os
from dotenv import load_dotenv

# Loading settings from an .env file
load_dotenv()
print("Loaded DATABASE_URL from .env:", os.getenv('DATABASE_URL'))  # للتأكد من تحميل .env

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY', True)
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', False)
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')
    REMEMBER_COOKIE_DURATION = int(os.getenv('REMEMBER_COOKIE_DURATION', 86400))
>>>>>>> d1b9626457fb9e49c0350bd926779b3f4fbfd806
