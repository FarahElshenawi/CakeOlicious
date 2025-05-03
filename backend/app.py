import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from backend.extensions import db, jwt
from backend.routes import (
    admin,
    auth,
    cart,
    checkout,
    orders,
    payments,
    products,
    reviews,
)
from backend.config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt.init_app(app)

# Register blueprints
app.register_blueprint(admin.bp, url_prefix="/admin")
app.register_blueprint(auth.bp, url_prefix="/auth")
app.register_blueprint(cart.bp, url_prefix="/cart")
app.register_blueprint(checkout.bp, url_prefix="/checkout")
app.register_blueprint(orders.bp, url_prefix="/orders")
app.register_blueprint(payments.bp, url_prefix="/payments")
app.register_blueprint(products.bp, url_prefix="/products")
app.register_blueprint(reviews.bp, url_prefix="/reviews")


@app.route("/")
def home():
    return {"message": "Welcome to the Cakeolicious API!"}


if __name__ == "__main__":
    app.run(debug=True)
