<<<<<<< HEAD
from backend.extensions import db

# Import all models here
from .user import User
from .product import Product
from .category import Category
from .cart import Cart
from .order import Order
from .order_detail import OrderDetail
from .payment import Payment
from .product_review import ProductReview


# models/__init__.py
# ملف فارغ
=======
# backend/models/__init__.py
from .Cart import Cart
from .Category import Category
from .Order import Order
from .OrderDetail import OrderDetail
from .Payment import Payment
from .Product import Product
from .ProductReview import ProductReview
from .User import User
>>>>>>> d1b9626457fb9e49c0350bd926779b3f4fbfd806
