<<<<<<< HEAD
# # routes/__init__.py
# from .admin import admin
# from .auth import auth
# from .cart import cart
# from .checkout import checkout
# from .orders import orders
# from .payments import payments
# from .products import products
# from .reviews import reviews

from flask import Flask
from flask_jwt_extended import JWTManager

jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    from backend.models import db
    db.init_app(app)
    for rule in app.url_map.iter_rules():
        print(rule)
    jwt.init_app(app)
    return app


# This file makes the backend directory a Python package
=======
from flask import Flask
from flask_migrate import Migrate
from backend.extensions import db
from backend.routes.auth import auth_bp
from backend.routes.orders import order_bp
from backend.routes.products import product_bp
from backend.routes.cart import cart_bp
from backend.routes.payments import payment_bp
from backend.routes.reviews import review_bp
from backend.routes.checkout import checkout_bp
from backend.routes.admin import admin_bp

def create_app():
    # Create a Flask app with templates and static locating
    app = Flask(__name__, 
                template_folder="../frontend/templates", 
                static_folder="../frontend/static")
    
    # Download settings from config.py
    app.config.from_object('backend.config.config')
    
    # Link SQLAlchemy to the app
    db.init_app(app)
    
    # Set up Flask-Migrate to manage database changes
    Migrate(app, db)
    
    # Blueprints Registration
    app.register_blueprint(auth_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(admin_bp)
    
    # Create tables in the database
    with app.app_context():
        db.create_all()
    
    return app
>>>>>>> d1b9626457fb9e49c0350bd926779b3f4fbfd806
