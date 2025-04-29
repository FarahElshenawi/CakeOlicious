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
from extensions import get_db_connection

class ProductReview:
    @staticmethod
    def add_review(product_name, username, rating, review_text):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "EXEC AddProductReview @ProductName=?, @Username=?, @Rating=?, @ReviewText=?",
                (product_name, username, rating, review_text)
            )
            result = cursor.fetchval()
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_review(product_name, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("EXEC GetProductReview @ProductName=?, @Username=?", (product_name, username))
            result = cursor.fetchall()
            if not result:
                return {"message": "لا توجد مراجعة لهذا المنتج."}
            columns = [column[0] for column in cursor.description]
            review = [dict(zip(columns, row)) for row in result]
            return review
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_review(product_name, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("EXEC DeleteProductReview @ProductName=?, @Username=?", (product_name, username))
            result = cursor.fetchval()
            conn.commit()
            return {"message": result}
        finally:
            cursor.close()
            conn.close()