 
# app/routes/auth.py

from flask import Blueprint,render_template, request, jsonify
from backend.extensions import db
from backend.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)
# ===== SHOW SIGNUP PAGE =====
@auth_bp.route('/signup', methods=['GET'])
def show_signup_form():
    return render_template('signup.html') 
# ===== SIGNUP =====
@auth_bp.route('/signup', methods=['POST'])
def signup():
   try:
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('pass_word')
    email = data.get('email')
    full_name = data.get('full_name')  # إضافة full_name
    user_address = data.get('user_address')  # إضافة user_address
    phone_number = data.get('phone_number')  # إضافة phone_number
    user_role = data.get('user_role')
    print(f"Received data: {data}")
    if not username or not password or not email:
            return jsonify({'message': 'Missing required fields'}), 400
    # التأكد من أن العمود في قاعدة البيانات هو 'username' وليس 'userName'
    if User.query.filter_by(username=username).first():  # تعديل هنا
            return jsonify({'message': 'Username already exists'}), 400
    if user_role not in ['Customer', 'admin']:  # التحقق هنا
        return jsonify({'message': 'Invalid role value'}), 400
    hashed_password = generate_password_hash(password)

    new_user = User(
            username=username,
            pass_word=hashed_password,
            email=email,
            full_name=full_name,  # إضافة full_name
            user_address=user_address,  # إضافة user_address
            phone_number=phone_number,  # إضافة phone_number
            user_role=user_role 
            

        )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
   except Exception as e:
        print("Error occurred:", str(e))  # Print the error in terminal
        return jsonify({'message': 'Internal Server Error'}), 500
    
# ===== LOGIN =====
@auth_bp.route('/login', methods=['POST'])
def login():
     try:
        data = request.get_json(force=True)
        username = data.get('username')
        password = data.get('pass_word')

        if not username or not password:
            return jsonify({'message': 'Missing username or password'}), 400

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.pass_word, password):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

     except Exception as e:
        print("Login Error occurred:", str(e))
        return jsonify({'message': f'Internal Server Error: {str(e)}'}), 500