from app.extensions import db

class Category(db.Model):
    __tablename__ = 'category'

    categoryID = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    products = db.relationship('Product', backref='category', lazy=True)
