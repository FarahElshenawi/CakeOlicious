
from backend.extensions import db


class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    @staticmethod
    def get_order_details(order_id):
        details = OrderDetail.query.filter_by(order_id=order_id).all()
        return [
            {
                "id": d.id,
                "order_id": d.order_id,
                "product_id": d.product_id,
                "quantity": d.quantity,
                "price": float(d.price),
            }
            for d in details
        ]
