# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Cart(db.Model):
#     __tablename__ = 'Cart'
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Numeric(10, 2), nullable=False)
#     discount = db.Column(db.Numeric(5, 2), default=0)
#     added_date = db.Column(db.DateTime, server_default=db.func.now())
# models/cart.py
from extensions import get_db_connection

class Cart:
    @staticmethod
    def get_cart_details(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("EXEC GetCartDetails @UserID=?", (user_id,))
            result = cursor.fetchall()
            if not result:
                return {"message": "العربة فارغة أو المستخدم غير موجود."}
            columns = [column[0] for column in cursor.description]
            cart_items = [dict(zip(columns, row)) for row in result]
            return cart_items
        finally:
            cursor.close()
            conn.close()