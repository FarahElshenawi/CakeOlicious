# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Category(db.Model):
#     __tablename__ = 'categories'
    
#     id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String(50), nullable=False)
#     category_description = db.Column(db.Text)
# models/category.py
from extensions import get_db_connection

class Category:
    @staticmethod
    def get_all_categories():
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM categories")
            categories = cursor.fetchall()
            return [{"id": c.id, "name": c.category_name, "description": c.category_description} for c in categories]
        finally:
            cursor.close()
            conn.close()