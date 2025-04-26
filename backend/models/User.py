from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False, unique=True)
    passWord = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True)
    fullName = db.Column(db.String(100))
    address = db.Column(db.String(255))
    phoneNum = db.Column(db.String(20))
    role = db.Column(db.String(20))  # Admin or Customer, مثلاً

    orders = db.relationship('Order', backref='user', lazy=True)
    reviews = db.relationship('ProductReview', backref='reviewer', lazy=True)
    cart_items = db.relationship('Cart', backref='user', lazy=True)

    def set_password(self, password):
        self.passWord = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passWord, password)

