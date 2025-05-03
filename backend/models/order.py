
from backend.extensions import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    @staticmethod
    def get_user_orders(user_id):
        orders = Order.query.filter_by(user_id=user_id).all()
        return [
            {
                "id": o.id,
                "user_id": o.user_id,
                "order_date": o.order_date.isoformat(),
                "total_amount": float(o.total_amount),
                "status": o.status,
            }
            for o in orders
        ]
