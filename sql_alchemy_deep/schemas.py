from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_smorest.fields import Upload
import marshmallow as ma
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

    author = ma.fields.Number()


class MultipartFileSchema(ma.Schema):
    file_1 = Upload()
