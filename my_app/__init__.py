from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "workouts"

def create_app():
  app = Flask(__name__)

  # Configuration
  app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://alouiseq@localhost/{DB_NAME}'
#  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to disable modification tracking
  db.init_app(app)

  # Initialize SQLAlchemy
  migrate = Migrate(app, db)

  # Import routes (after creating the app to avoid circular imports)
  from . import routes

  return app
