 # routes/review.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.product_review import ProductReview
from models.user import User

bp = Blueprint('review', __name__)

@bp.route('/add', methods=['POST'])
@jwt_required()
def add_review():
    current_user = get_jwt_identity()
    data = request.get_json()
    product_name = data.get('product_name')
    rating = data.get('rating')
    review_text = data.get('review_text')

    if not all([product_name, rating]):
        return jsonify({"message": "حقول مطلوبة مفقودة"}), 400

    result = ProductReview.add_review(product_name, current_user, rating, review_text)
    return jsonify(result), 201

@bp.route('/get', methods=['GET'])
@jwt_required()
def get_review():
    current_user = get_jwt_identity()
    product_name = request.args.get('product_name')
    if not product_name:
        return jsonify({"message": "اسم المنتج مطلوب"}), 400

    result = ProductReview.get_review(product_name, current_user)
    return jsonify(result)

@bp.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_review():
    current_user = get_jwt_identity()
    product_name = request.args.get('product_name')
    if not product_name:
        return jsonify({"message": "اسم المنتج مطلوب"}), 400

    result = ProductReview.delete_review(product_name, current_user)
    return jsonify(result)
