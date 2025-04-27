import os
from dotenv import load_dotenv
import urllib


load_dotenv()

class Config:
    DRIVER = os.getenv('DRIVER')
    SERVER = os.getenv('SERVER')
    DATABASE = os.getenv('DATABASE')
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    CONNECTION_STRING = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(CONNECTION_STRING)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
