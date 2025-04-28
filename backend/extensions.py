from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
sys.path.append('C:/Fara7 repo/CakeOlicious/venv/Lib/site-packages')

db = SQLAlchemy()
migrate = Migrate()
