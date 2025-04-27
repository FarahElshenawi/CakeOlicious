from backend.extensions import db

class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    orderDetailID = db.Column(db.Integer, primary_key=True)
    
    orderID = db.Column(db.Integer, db.ForeignKey('orders.orderID'), nullable=False)
    productID = db.Column(db.Integer, db.ForeignKey('products.productID'), nullable=False)
    
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    order = db.relationship('Order', backref=db.backref('order_details', lazy=True))
    product = db.relationship('Product', backref=db.backref('order_details', lazy=True))
