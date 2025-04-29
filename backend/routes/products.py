# from flask import Blueprint, request, jsonify
# from app.extensions import db
# from app.models.product import Product

# products_bp = Blueprint('products', __name__)

# # ===== ADD PRODUCT =====
# @products_bp.route('/products', methods=['POST'])
# def add_product():
#     data = request.get_json()
#     name = data.get('name')
#     description = data.get('description')
#     price = data.get('price')
#     stock = data.get('stock')

#     if not name or not price or not stock:
#         return jsonify({'message': 'Missing required fields'}), 400

#     new_product = Product(
#         name=name,
#         description=description,
#         price=price,
#         stock=stock
#     )

#     db.session.add(new_product)
#     db.session.commit()

#     return jsonify({'message': 'Product added successfully'}), 201

# # ===== GET ALL PRODUCTS =====
# @products_bp.route('/products', methods=['GET'])
# def get_all_products():
#     products = Product.query.all()
#     return jsonify([{
#         'id': p.id,
#         'name': p.name,
#         'description': p.description,
#         'price': p.price,
#         'stock': p.stock
#     } for p in products])

# # ===== GET PRODUCT BY ID =====
# @products_bp.route('/products/<int:id>', methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404

#     return jsonify({
#         'id': product.id,
#         'name': product.name,
#         'description': product.description,
#         'price': product.price,
#         'stock': product.stock
#     })

# # ===== UPDATE PRODUCT =====
# @products_bp.route('/products/<int:id>', methods=['PUT'])
# def update_product(id):
#     product = Product.query.get(id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404

#     data = request.get_json()
#     product.name = data.get('name', product.name)
#     product.description = data.get('description', product.description)
#     product.price = data.get('price', product.price)
#     product.stock = data.get('stock', product.stock)

#     db.session.commit()

#     return jsonify({'message': 'Product updated successfully'})

# # ===== DELETE PRODUCT =====
# @products_bp.route('/products/<int:id>', methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get(id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404

#     db.session.delete(product)
#     db.session.commit()

#     return jsonify({'message': 'Product deleted successfully'})
 
# routes/products.py
from flask import Blueprint, jsonify
from models.product import Product
from models.category import Category

bp = Blueprint('products', __name__)

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.get_all_products()
    return jsonify(products)

@bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.get_all_categories()
    return jsonify(categories)