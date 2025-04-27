from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductReview(db.Model):
    __tablename__ ='product_reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer)
    review_text = db.Column(db.Text)
    review_date = db.Column(db.DateTime, server_default=db.func.now())
