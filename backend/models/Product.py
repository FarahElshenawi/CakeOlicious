from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    productID = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float, default=0.0)
    image_URL = db.Column(db.String(255))
    
    categoryID = db.Column(db.Integer, db.ForeignKey('category.categoryID'))

    cart_items = db.relationship('Cart', backref='product', lazy=True)
   # order_items = db.relationship('OrderDetail', backref='product', lazy=True)
