from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from . import db
from .models import User
from .schemas import UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/', methods=['POST'])
def create_user():
    user_schema = UserSchema()
    try:
        user = user_schema.load(request.json, session=db.session)
        existing_user = User.query.filter_by(email=user.email).first()

        if existing_user:
            return jsonify({'message': 'Email already exists'}), 409

        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema.dump(user)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400


@users_bp.route('/', methods=['GET'])
def get_users():
    user_schema = UserSchema()

    users = User.query.all()
    return user_schema.dump(users, many=True), 200
