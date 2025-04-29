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

class Config:
    SQL_CONNECTION_STRING = 'Driver={ODBC Driver 17 for SQL Server};Server=your_server;Database=your_db;Trusted_Connection=yes;'
    SECRET_KEY = os.getenv('SECRET_KEY', '3a6a30088abd611bcdffd19791fb46fac41dc107ff63670e179073926b5711e7')  # استبدل بمفتاح آمن
    SQL_SERVER = "MahmoudsPC\SQLEXPRESS"  # استبدل باسم خادم SQL Server الخاص بك
    #SQL_SERVER = "localhost\\SQLEXPRESS"
    SQL_DATABASE = "Sweets_Store"
    SQL_USER = "MAHMOUDSPC\DELL"  # استبدل باسم المستخدم لـ SQL Server
    SQL_PASSWORD = None  # استبدل بكلمة المرور لـ SQL Server
    SQL_CONNECTION_STRING = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER};"
        f"PWD={SQL_PASSWORD}"
    )
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '7aefd18aa561b894f2acbf95c40b957c070efa1ca7b37293d2435cfe893ac327')  # استبدل بمفتاح آمن
# import secrets
# print(secrets.token_hex(32))
