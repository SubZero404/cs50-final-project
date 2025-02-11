from flask import Flask, send_from_directory
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sub_zero'

    @app.route('/node_modules/<path:filename>')
    def serve_node_modules(filename):
        return send_from_directory(os.path.join(app.root_path, '..', 'node_modules'), filename)

    from .views import views
    from .admin import admin
    from .auth import auth

    app.register_blueprint(views, prefix='/')
    app.register_blueprint(admin, prefix='/admin')
    app.register_blueprint(auth, prefix='/')

    return app