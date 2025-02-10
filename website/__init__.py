from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sub_zero'

    from .views import views
    from .admin import admin
    from .auth import auth

    app.register_blueprint(views, prefix='/')
    app.register_blueprint(admin, prefix='/')
    app.register_blueprint(auth, prefix='/')

    return app