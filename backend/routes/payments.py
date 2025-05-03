# routes/payments.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models.payment import Payment

bp = Blueprint("payments", __name__)


@bp.route("/<int:order_id>", methods=["GET"])
@jwt_required()
def get_payment(order_id):
    payment = Payment.get_payment_by_order(order_id)
    if not payment:
        return jsonify({"message": "الدفع غير موجود"}), 404
    return jsonify(payment)
