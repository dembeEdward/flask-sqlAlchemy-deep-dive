from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import getenv

db = SQLAlchemy()
migration = Migrate()

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    db.init_app(app)

    from .models import User
    from .users import users_bp
    from .posts import posts_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)

    migration.init_app(app, db)

    return app
