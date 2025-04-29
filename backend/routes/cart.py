 # routes/cart.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.cart import Cart
from models.user import User

bp = Blueprint('cart', __name__)

@bp.route('/details', methods=['GET'])
@jwt_required()
def get_cart_details():
    current_user = get_jwt_identity()
    user = User.get_user_by_username(current_user)
    if not user:
        return jsonify({"message": "المستخدم غير موجود"}), 404

    result = Cart.get_cart_details(user['id'])
    return jsonify(result)
