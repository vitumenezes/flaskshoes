from .models import User


def init_app(app):
    @app.route('/')
    def index():
        return 'just setting up'
