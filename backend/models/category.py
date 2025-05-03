
from backend.extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    @staticmethod
    def get_all_categories():
        categories = Category.query.all()
        return [
            {"id": c.id, "name": c.category_name, "description": c.description}
            for c in categories
        ]
