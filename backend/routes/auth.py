 
# app/routes/auth.py
from flask import Blueprint,render_template, request, jsonify
from app.extensions import db
from app.models.User import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)
# ===== SHOW SIGNUP PAGE =====
@auth_bp.route('/signup', methods=['GET'])
def show_signup_form():
    return render_template('signup.html') 
# ===== SIGNUP =====
@auth_bp.route('/signup', methods=['POST'])
def signup():
   data = request.get_json()
   username = data.get('userName')
   password = data.get('passWord')
   email = data.get('email')

   if User.query.filter_by(userName=username).first():
        return jsonify({'message': 'Username already exists'}), 400

   hashed_password = generate_password_hash(password)

   new_user = User(
        userName=username,
        passWord=hashed_password,
        email=email
    )

   db.session.add(new_user)
   db.session.commit()

   return jsonify({'message': 'User created successfully'}), 201


# ===== LOGIN =====
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('userName')
    password = data.get('passWord')

    user = User.query.filter_by(userName=username).first()
    if user and check_password_hash(user.passWord, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
