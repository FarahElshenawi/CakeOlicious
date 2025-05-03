# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Product(db.Model):
#     __tablename__ = 'products'

#     id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(100), nullable=False)
#     product_description = db.Column(db.Text)
#     price = db.Column(db.Numeric(10, 2), nullable=False)
#     stock = db.Column(db.Integer, nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
#     image_url = db.Column(db.String(255))
#     discount = db.Column(db.Numeric(5, 2), default=0)

# models/product.py
from backend.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    image_url = db.Column(db.String(255))
    discount = db.Column(db.Numeric(5, 2), default=0)

    @staticmethod
    def add_product(
        product_name, description, price, stock, category_id, image_url, discount
    ):
        product = Product(
            product_name=product_name,
            description=description,
            price=price,
            stock=stock,
            category_id=category_id,
            image_url=image_url,
            discount=discount,
        )
        db.session.add(product)
        db.session.commit()
        return {"message": "Product added successfully"}

    @staticmethod
    def update_price(product_name, new_price):
        product = Product.query.filter_by(product_name=product_name).first()
        if product:
            product.price = new_price
            db.session.commit()
            return {"message": "Price updated successfully"}
        return {"message": "Product not found"}, 404

    @staticmethod
    def add_discount(product_name, new_discount):
        product = Product.query.filter_by(product_name=product_name).first()
        if product:
            product.discount = new_discount
            db.session.commit()
            return {"message": "Discount added successfully"}
        return {"message": "Product not found"}, 404

    @staticmethod
    def get_all_products():
        products = Product.query.all()
        return [
            {
                "id": p.id,
                "name": p.product_name,
                "description": p.description,
                "price": float(p.price),
                "stock": p.stock,
                "category_id": p.category_id,
                "image_url": p.image_url,
                "discount": float(p.discount),
            }
            for p in products
        ]
