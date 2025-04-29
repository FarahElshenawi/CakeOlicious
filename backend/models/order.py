# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Order(db.Model):
#     __tablename__ ='orders'
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     order_date = db.Column(db.DateTime, server_default=db.func.now())
#     total_amount = db.Column(db.Numeric(10, 2), nullable=False)
#     status = db.Column(db.String(20), nullable=False)
# models/order.py
from extensions import get_db_connection

class Order:
    @staticmethod
    def get_user_orders(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
            orders = cursor.fetchall()
            return [{"id": o.id, "user_id": o.user_id, "order_date": str(o.order_date), "total_amount": float(o.total_amount), "status": o.status} for o in orders]
        finally:
            cursor.close()
            conn.close()