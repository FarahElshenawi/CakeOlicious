from app.extensions import db

class Payment(db.Model):
    __tablename__ = 'payment'

    paymentID = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Paid, Failed, Pending, etc

    orderID = db.Column(db.Integer, db.ForeignKey('orders.orderID'), nullable=False)

    order = db.relationship('Order', backref=db.backref('payment', uselist=False))
