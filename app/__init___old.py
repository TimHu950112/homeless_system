from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '請先登入以訪問此頁面。'

    # 註冊藍圖
    from app.routes import main, auth, accommodation, hygiene, food, courses, health, employment, welfare, admin

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(accommodation.bp)
    app.register_blueprint(hygiene.bp)
    app.register_blueprint(food.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(health.bp)
    app.register_blueprint(employment.bp)
    app.register_blueprint(welfare.bp)
    app.register_blueprint(admin.bp)

    with app.app_context():
        db.create_all()

    return app
