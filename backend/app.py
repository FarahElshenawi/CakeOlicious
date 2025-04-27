from flask import Flask
from backend.routes.auth import auth_bp
from backend.extensions import db, migrate
from flask_migrate import Migrate
from backend.config.config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.config.Config')
    migrate = Migrate(app, db)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
