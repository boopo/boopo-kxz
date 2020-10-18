from flask import Blueprint, render_template

blue = Blueprint('blue', __name__)


def init_view(app):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return render_template('index.html')

