import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    '''Base configuration class'''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL= os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
