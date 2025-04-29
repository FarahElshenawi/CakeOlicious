# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Payment(db.Model):
#     __tablename__ = 'payments'
    
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
#     payment_date = db.Column(db.DateTime, server_default=db.func.now())
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     payment_method = db.Column(db.String(20), nullable=False)
#     status = db.Column(db.String(20), nullable=False)
# models/payment.py
from extensions import get_db_connection

class Payment:
    @staticmethod
    def get_payment_by_order(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM payments WHERE order_id = ?", (order_id,))
            payment = cursor.fetchone()
            if payment:
                return {
                    "id": payment.id,
                    "order_id": payment.order_id,
                    "payment_date": str(payment.payment_date),
                    "amount": float(payment.amount),
                    "payment_method": payment.payment_method,
                    "status": payment.status
                }
            return None
        finally:
            cursor.close()
            conn.close()