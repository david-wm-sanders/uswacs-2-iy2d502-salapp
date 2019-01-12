"""Flask salapp."""
from flask import Flask
from .config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors

# TODO: add Content-Security-Policy and Content-Security-Policy-Report-Only headers
# TODO: improve app with better comments and parameter hints in docstrings
