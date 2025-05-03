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
