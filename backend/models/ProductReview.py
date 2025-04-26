from app.extensions import db

class ProductReview(db.Model):
    __tablename__ = 'product_review'

    productID = db.Column(db.Integer, db.ForeignKey('products.productID'), primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), primary_key=True)
    review_date = db.Column(db.DateTime)
    rating = db.Column(db.Integer)
    reviewText = db.Column(db.Text)
    
    product = db.relationship('Product', backref='product_reviews', lazy=True)  # تم تعديل backref هنا
    # تم حذف user العلاقة بسبب تعارض الـ backref في ProductReview
