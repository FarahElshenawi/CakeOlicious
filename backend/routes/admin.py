# routes/admin.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models.product import Product
from backend.models.user import User

bp = Blueprint("admin", __name__)


@bp.route("/add-product", methods=["POST"])
@jwt_required()
def add_product():
    current_user = get_jwt_identity()
    user = User.get_user_by_username(current_user)
    if user["role"] != "Admin":
        return jsonify({"message": "يتطلب صلاحيات المسؤول"}), 403

    data = request.get_json()
    product_name = data.get("product_name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")
    category_id = data.get("category_id")
    image_url = data.get("image_url")
    discount = data.get("discount", 0)

    if not all([product_name, price, stock, category_id]):
        return jsonify({"message": "حقول مطلوبة مفقودة"}), 400

    result = Product.add_product(
        product_name, description, price, stock, category_id, image_url, discount
    )
    return jsonify(result), 201


@bp.route("/update-price", methods=["PUT"])
@jwt_required()
def update_price():
    current_user = get_jwt_identity()
    user = User.get_user_by_username(current_user)
    if user["role"] != "Admin":
        return jsonify({"message": "يتطلب صلاحيات المسؤول"}), 403

    data = request.get_json()
    product_name = data.get("product_name")
    new_price = data.get("new_price")

    if not all([product_name, new_price]):
        return jsonify({"message": "حقول مطلوبة مفقودة"}), 400

    result = Product.update_price(product_name, new_price)
    return jsonify(result)


@bp.route("/add-discount", methods=["PUT"])
@jwt_required()
def add_discount():
    current_user = get_jwt_identity()
    user = User.get_user_by_username(current_user)
    if user["role"] != "Admin":
        return jsonify({"message": "يتطلب صلاحيات المسؤول"}), 403

    data = request.get_json()
    product_name = data.get("product_name")
    new_discount = data.get("new_discount")

    if not all([product_name, new_discount]):
        return jsonify({"message": "حقول مطلوبة مفقودة"}), 400

    result = Product.add_discount(product_name, new_discount)
    return jsonify(result)
