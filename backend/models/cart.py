
# models/cart.py
from backend.extensions import db
from datetime import datetime


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Numeric(5, 2), default=0)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_cart_details(user_id):
        cart_items = Cart.query.filter_by(user_id=user_id).all()
        if not cart_items:
            return {"message": "Cart is empty or user not found."}

        return [
            {
                "id": item.id,
                "user_id": item.user_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": float(item.price),
                "discount": float(item.discount),
                "added_date": item.added_date.isoformat(),
            }
            for item in cart_items
        ]
