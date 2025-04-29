# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class OrderDetail(db.Model):
#     __tablename__ = 'order_details'
    
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Numeric(10, 2), nullable=False)
# models/order_detail.py
from extensions import get_db_connection

class OrderDetail:
    @staticmethod
    def get_order_details(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM order_details WHERE order_id = ?", (order_id,))
            details = cursor.fetchall()
            return [{"id": d.id, "order_id": d.order_id, "product_id": d.product_id, "quantity": d.quantity, "price": float(d.price)} for d in details]
        finally:
            cursor.close()
            conn.close()