from flask.views import MethodView
from flask_smorest import Blueprint, abort
from werkzeug.utils import secure_filename
from . import db
from .schemas import PostSchema, MultipartFileSchema
from .models import Post
from os import path

posts_bp = Blueprint('posts', __name__, url_prefix='/posts',
                     description='Operations on posts')


@posts_bp.route('/')
class Posts(MethodView):
    @posts_bp.arguments(PostSchema)
    @posts_bp.response(201, PostSchema)
    def post(self, post):
        """Add a new post"""
        db.session.add(post)
        db.session.commit()
        return post, 201

    @posts_bp.response(200, PostSchema(many=True))
    def get(self):
        posts = Post.query.all()
        return posts, 200


@posts_bp.route('/<int:id>')
class PostById(MethodView):
    @posts_bp.response(200, PostSchema)
    def get(self, id):
        """Get a post by id"""
        post = Post.query.get_or_404(id)
        return post, 200

    @posts_bp.arguments(PostSchema)
    @posts_bp.response(200, PostSchema)
    def put(self, post_update, id):
        """Update a post by id"""
        post = Post.query.get_or_404(id)
        post.title = post_update.title
        post.content = post_update.content
        db.session.commit()
        return post, 200


@posts_bp.route('/image', methods=['POST'])
@posts_bp.arguments(MultipartFileSchema, location='files')
@posts_bp.response(201, PostSchema)
def upload_image(files):
    """Upload an image"""
    try:
        base_dir = 'static'
        file_1 = files['file_1']
        file_1.save(path.join(base_dir, secure_filename(file_1.filename)))
    except KeyError:
        abort(400, message='No file part')
