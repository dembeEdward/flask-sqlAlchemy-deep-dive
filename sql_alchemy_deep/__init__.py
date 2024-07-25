from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from dotenv import load_dotenv
from os import getenv

db = SQLAlchemy()
migration = Migrate()

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['API_TITLE'] = 'Blog API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'

    db.init_app(app)

    from .models import User
    from .users import users_bp
    from .posts import posts_bp

    api = Api(app)

    api.register_blueprint(users_bp)
    api.register_blueprint(posts_bp)

    migration.init_app(app, db)

    return app
