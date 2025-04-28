import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DRIVER = os.environ.get('DRIVER')
    SERVER = os.environ.get('SERVER')
    DATABASE = os.environ.get('DATABASE')
    DRIVER = DRIVER.replace(' ', '+')
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
