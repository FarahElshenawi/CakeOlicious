# routes/orders.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.order import Order
from backend.models.user import User

bp = Blueprint("orders", __name__)


@bp.route("/", methods=["GET"])
@jwt_required()
def get_orders():
    current_user = get_jwt_identity()
    user = User.get_user_by_username(current_user)
    if not user:
        return jsonify({"message": "User not found"}), 404

    orders = Order.get_user_orders(user["id"])
    return jsonify(orders)
