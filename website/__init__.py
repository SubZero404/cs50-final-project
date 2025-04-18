from flask import Flask, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_migrate import Migrate

import os

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sub_zero'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(404)
    def pageNotFound(error):
        return render_template('404.html')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from website.models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .views import views
    from .admin import admin 
    from .auth import auth

    app.register_blueprint(views, url_prefix='')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

    

    @app.route('/node_modules/<path:filename>')
    def serve_node_modules(filename):
        return send_from_directory(os.path.join(app.root_path, '..', 'node_modules'), filename)

    # with app.app_context():
    #     create_database()


    # def create_database():
    #     if not os.path.exists('website/' + DB_NAME):
    #         from .models import User, Category, Product, Image, Review, Cart, Order, OrderItem
    #         db.create_all()
    #         print('Database created!')

    
    return app