from backend.extensions import db

class Order(db.Model):
    __tablename__ = 'orders'

    orderID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    totalAmount = db.Column(db.Float)
    status = db.Column(db.String(50))
    orderDate = db.Column(db.DateTime)

    #order_details = db.relationship('OrderDetail', backref='order', lazy=True)
    #payment = db.relationship('Payment', backref='order', uselist=False)
