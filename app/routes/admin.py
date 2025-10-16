from flask import Blueprint, render_template
from flask_login import login_required
from app.database import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def dashboard():
    # 統計數據
    total_users = db.count('users')
    total_bookings = db.count('accommodation_bookings')
    pending_bookings = db.count('accommodation_bookings', status='pending')

    # 計算總點數
    all_users = db.find('users')
    total_points = sum(user.get('points', 0) for user in all_users)

    # 最新預約
    all_bookings = db.find('accommodation_bookings')
    all_bookings.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    recent_bookings = all_bookings[:5]

    # 為預約添加用戶和住宿名稱
    for booking in recent_bookings:
        user = db.get_by_id('users', booking.get('user_id'))
        booking['user_name'] = user.get('username') if user else 'Unknown'
        accommodation = db.get_by_id('accommodations', booking.get('accommodation_id'))
        booking['accommodation_name'] = accommodation.get('name') if accommodation else 'Unknown'

    # 最新用戶
    all_users.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    recent_users = all_users[:5]

    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_bookings=total_bookings,
                         pending_bookings=pending_bookings,
                         total_points=total_points,
                         recent_bookings=recent_bookings,
                         recent_users=recent_users)
