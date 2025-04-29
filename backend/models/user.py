# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True, nullable=False)
#     pass_word = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     full_name = db.Column(db.String(100), nullable=False)
#     user_address = db.Column(db.Text)
#     phone_number = db.Column(db.String(20))
#     user_role = db.Column(db.String(20), nullable=False)
# models/user.py
from extensions import get_db_connection

class User:
    @staticmethod
    def add_user(username, password, email, full_name, address=None, phone_number=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "EXEC add_customer @username=?, @pass_word=?, @email=?, @full_name=?, @user_address=?, @phone_number=?",
                (username, password, email, full_name, address, phone_number)
            )
            result = cursor.fetchval()  # الحصول على الرسالة من الإجراء المخزن
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_user_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "password": user.pass_word,
                    "email": user.email,
                    "full_name": user.full_name,
                    "address": user.user_address,
                    "phone_number": user.phone_number,
                    "role": user.user_role
                }
            return None
        finally:
            cursor.close()
            conn.close()