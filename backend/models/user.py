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
from backend.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    role = db.Column(db.String(20), nullable=False, default="user")

    @staticmethod
    def add_user(username, password, email, full_name, address=None, phone_number=None):
        user = User(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
            address=address,
            phone_number=phone_number,
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}

    @staticmethod
    def get_user_by_username(username):
        user = User.query.filter_by(username=username).first()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "full_name": user.full_name,
                "address": user.address,
                "phone_number": user.phone_number,
                "role": user.role,
            }
        return None
