
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models.user import User

bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    full_name = data.get("full_name")
    address = data.get("address")
    phone_number = data.get("phone_number")

    if not all([username, password, email, full_name]):
        return jsonify({"message": "Required fields are missing"}), 400

    hashed_password = generate_password_hash(password)
    result = User.add_user(
        username, hashed_password, email, full_name, address, phone_number
    )
    return jsonify(result), 201


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not all([username, password]):
        return jsonify({"message": "Username or password is missing"}), 400

    user = User.get_user_by_username(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid login credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200
