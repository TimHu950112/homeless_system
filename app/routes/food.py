from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.database import db

bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/')
def index():
    providers = db.find('food_providers', is_active=True)
    return render_template('food/index.html', providers=providers)

@bp.route('/my-vouchers')
@login_required
def my_vouchers():
    vouchers = db.find('meal_vouchers', user_id=current_user.id)
    return render_template('food/my_vouchers.html', vouchers=vouchers)
