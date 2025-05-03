# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class ProductReview(db.Model):
#     __tablename__ ='product_reviews'

#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     rating = db.Column(db.Integer)
#     review_text = db.Column(db.Text)
#     review_date = db.Column(db.DateTime, server_default=db.func.now())

# models/product_review.py
from backend.extensions import db
from datetime import datetime
from backend.models.product import Product
from backend.models.user import User


class ProductReview(db.Model):
    __tablename__ = "product_reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    rating = db.Column(db.Integer)
    review_text = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def add_review(product_name, username, rating, review_text):
        product = Product.query.filter_by(product_name=product_name).first()
        user = User.query.filter_by(username=username).first()

        if not product or not user:
            return {"message": "Product or user not found"}

        review = ProductReview(
            product_id=product.id,
            user_id=user.id,
            rating=rating,
            review_text=review_text,
        )
        db.session.add(review)
        db.session.commit()
        return {"message": "Review added successfully"}

    @staticmethod
    def get_review(product_name, username):
        product = Product.query.filter_by(product_name=product_name).first()
        user = User.query.filter_by(username=username).first()

        if not product or not user:
            return {"message": "Product or user not found"}

        review = ProductReview.query.filter_by(
            product_id=product.id, user_id=user.id
        ).first()

        if not review:
            return {"message": "No review found for this product"}

        return {
            "id": review.id,
            "product_id": review.product_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "review_text": review.review_text,
            "review_date": review.review_date.isoformat(),
        }

    @staticmethod
    def delete_review(product_name, username):
        product = Product.query.filter_by(product_name=product_name).first()
        user = User.query.filter_by(username=username).first()

        if not product or not user:
            return {"message": "Product or user not found"}

        review = ProductReview.query.filter_by(
            product_id=product.id, user_id=user.id
        ).first()

        if not review:
            return {"message": "No review found to delete"}

        db.session.delete(review)
        db.session.commit()
        return {"message": "Review deleted successfully"}
