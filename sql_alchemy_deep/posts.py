from flask import Blueprint, request, jsonify
from . import db
from .schemas import PostSchema
from .models import Post

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')


@posts_bp.route('/', methods=['POST'])
def create_post():
    post_schema = PostSchema()

    try:
        post = post_schema.load(request.json, session=db.session)
        db.session.add(post)
        db.session.commit()

        return post_schema.dump(post), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


@posts_bp.route('/', methods=['GET'])
def get_posts():
    post_schema = PostSchema()

    posts = post_schema.dump(db.session.query(Post).all(), many=True)
    return jsonify(posts), 200
