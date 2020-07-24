from flask import render_template, request, Blueprint
from realmadrid_blog.models import Post
from realmadrid_blog.main.utils import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    #posortowanie malejąco, podział na stona 5 postów na stronę
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", posts=posts, logo=logo_picture(), image_file=profile_picture())


@main.route("/about")
def about():
    return render_template("about.html", title='About', logo=logo_picture(), image_file=profile_picture())

