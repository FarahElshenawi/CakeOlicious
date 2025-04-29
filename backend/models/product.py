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
from extensions import get_db_connection

class Product:
    @staticmethod
    def add_product(product_name, description, price, stock, category_id, image_url, discount):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "EXEC AddNewProduct @product_name=?, @description=?, @price=?, @stock=?, @category_id=?, @image_url=?, @discount=?",
                (product_name, description, price, stock, category_id, image_url, discount)
            )
            result = cursor.fetchval()
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_price(product_name, new_price):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "EXEC UpdateProductPrice @product_name=?, @new_price=?",
                (product_name, new_price)
            )
            result = cursor.fetchval()
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def add_discount(product_name, new_discount):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "EXEC AddProductDiscount @product_name=?, @new_discount=?",
                (product_name, new_discount)
            )
            result = cursor.fetchval()
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_products():
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return [{"id": p.id, "name": p.product_name, "description": p.product_description, "price": float(p.price), "stock": p.stock, "category_id": p.category_id, "image_url": p.image_url, "discount": float(p.discount)} for p in products]
        finally:
            cursor.close()
            conn.close()