from flask import Flask
from flask_login import LoginManager
from app.database import db
from app.seed_data import init_data

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '請先登入以訪問此頁面。'

    # 自動初始化數據
    with app.app_context():
        init_data()

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

    # 定義 user_loader
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.get_by_id(int(user_id))

    return app
