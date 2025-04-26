from app.extensions import db

class Cart(db.Model):
    __tablename__ = 'cart'

    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), primary_key=True)
    productID = db.Column(db.Integer, db.ForeignKey('products.productID'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    added_date = db.Column(db.DateTime)
    discount = db.Column(db.Float, default=0.0)
    
