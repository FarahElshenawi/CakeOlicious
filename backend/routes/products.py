
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models.product import Product
from backend.models.category import Category

bp = Blueprint("products", __name__)


@bp.route("/", methods=["GET"])
def get_products():
    products = Product.get_all_products()
    return jsonify(products)


@bp.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.get_all_categories()
    return jsonify(categories)
