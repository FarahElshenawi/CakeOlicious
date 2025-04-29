# from flask import Flask
# from backend.routes.auth import auth_bp
# from backend.extensions import db, migrate
# from flask_migrate import Migrate
# from backend.config.config import Config
# from flask import current_app
# import logging
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)  
#     print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
#     app.logger.setLevel(logging.DEBUG)
   
#     migrate = Migrate(app, db)
#     db.init_app(app)
#     migrate.init_app(app, db)

#     app.register_blueprint(auth_bp, url_prefix='/api/auth')

#     with app.app_context():
#         print(current_app.url_map)
    
#     @app.before_first_request
#     def check_db_connection():
#         try:
#             db.engine.connect()  
#             print("Database connection successful.")
#         except Exception as e:
#             print("Database connection error:", e)
#             app.logger.error(f"Database connection error: {str(e)}")
#     return app

# if __name__ == '__main__':
#     app = create_app()  
#     app.run(debug=True)  
# app.py
from flask import Flask
from extensions import get_db_connection, jwt
from routes import admin, auth, cart, checkout, orders, payments, products, reviews
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# تهيئة JWT
jwt.init_app(app)

# تسجيل المسارات (blueprints)
app.register_blueprint(admin.bp, url_prefix='/admin')
app.register_blueprint(auth.bp, url_prefix='/auth')
app.register_blueprint(cart.bp, url_prefix='/cart')
app.register_blueprint(checkout.bp, url_prefix='/checkout')
app.register_blueprint(orders.bp, url_prefix='/orders')
app.register_blueprint(payments.bp, url_prefix='/payments')
app.register_blueprint(products.bp, url_prefix='/products')
app.register_blueprint(reviews.bp, url_prefix='/reviews')

# مسار اختباري للتحقق من تشغيل التطبيق
@app.route('/')
def home():
    return {"message": "مرحبًا بك في واجهة برمجة تطبيقات متجر الحلويات!"}

if __name__ == '__main__':
    app.run(debug=True)