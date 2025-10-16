from flask import Blueprint, render_template, request
from flask_login import current_user
from app.database import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """首頁"""
    # 獲取各類服務的統計資訊
    total_accommodations = db.count('accommodations', is_active=True)
    total_food_providers = db.count('food_providers', is_active=True)
    total_courses = db.count('courses', is_active=True)
    total_jobs = db.count('jobs', is_active=True)
    total_welfare = db.count('welfare_programs', is_active=True)

    # 獲取最新資訊
    all_courses = db.find('courses', is_active=True)
    all_courses.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    recent_courses = all_courses[:3]

    all_jobs = db.find('jobs', is_active=True)
    all_jobs.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    recent_jobs = all_jobs[:3]

    return render_template('index.html',
                         total_accommodations=total_accommodations,
                         total_food_providers=total_food_providers,
                         total_courses=total_courses,
                         total_jobs=total_jobs,
                         total_welfare=total_welfare,
                         recent_courses=recent_courses,
                         recent_jobs=recent_jobs)


@bp.route('/about')
def about():
    """關於我們"""
    return render_template('about.html')


@bp.route('/contact')
def contact():
    """聯絡我們"""
    return render_template('contact.html')


@bp.route('/search')
def search():
    """全站搜尋"""
    query = request.args.get('q', '')
    return render_template('search.html', query=query)
