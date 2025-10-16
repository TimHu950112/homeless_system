from flask import Blueprint, render_template
from app.database import db

bp = Blueprint('health', __name__, url_prefix='/health')

@bp.route('/')
def index():
    providers = db.find('health_providers', is_active=True)
    return render_template('health/index.html', providers=providers)
