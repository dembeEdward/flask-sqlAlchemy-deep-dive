from flask_smorest import Blueprint
from flask.views import MethodView
from . import db
from .models import User
from .schemas import UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users',
                     description='Operations on users')


@users_bp.route('/')
class Users(MethodView):
    @users_bp.arguments(UserSchema)
    @users_bp.response(201, UserSchema)
    def post(self, user):
        db.session.add(user)
        db.session.commit()
        return user, 201

    @users_bp.response(200, UserSchema(many=True))
    def get(self):
        users = User.query.all()
        return users, 200
