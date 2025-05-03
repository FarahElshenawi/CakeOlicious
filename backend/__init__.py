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
    return app


# This file makes the backend directory a Python package
