from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_smorest.fields import Upload
import marshmallow
from .models import User, Post
from . import db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        sqla_session = db.session


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_relationships = True
        sqla_session = db.session


class MultipartFileSchema(marshmallow.Schema):
    file_1 = Upload()
