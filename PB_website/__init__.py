from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .web_views import web_views
    from .auth import auth

    app.register_blueprint(web_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Phone

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists('PB_website/' + DB_NAME):
        db.create_all(app=app)
        print('created Database!')
