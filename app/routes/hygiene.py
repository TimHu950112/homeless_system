from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from datetime import datetime
from app.database import db

bp = Blueprint('hygiene', __name__, url_prefix='/hygiene')

@bp.route('/')
def index():
    """盥洗設施列表"""
    district = request.args.get('district', '')
    facilities = db.find('hygiene_facilities', is_active=True)

    if district:
        facilities = [f for f in facilities if f.get('district') == district]

    return render_template('hygiene/index.html', facilities=facilities)


@bp.route('/<int:id>')
def detail(id):
    """設施詳情"""
    facility = db.get_by_id('hygiene_facilities', id)
    if not facility:
        flash('找不到該設施。', 'danger')
        return redirect(url_for('hygiene.index'))
    return render_template('hygiene/detail.html', facility=facility)


@bp.route('/<int:id>/book', methods=['GET', 'POST'])
@login_required
def book(id):
    """預約盥洗服務"""
    facility = db.get_by_id('hygiene_facilities', id)
    if not facility:
        flash('找不到該設施。', 'danger')
        return redirect(url_for('hygiene.index'))

    if request.method == 'POST':
        booking_date = datetime.strptime(request.form.get('booking_date'), '%Y-%m-%d').date()
        booking_time = request.form.get('booking_time')
        service_type = request.form.get('service_type')

        booking = {
            'user_id': current_user.id,
            'facility_id': facility['id'],
            'booking_date': booking_date.isoformat(),
            'booking_time': booking_time,
            'service_type': service_type,
            'status': 'confirmed'
        }

        db.insert('hygiene_bookings', booking)
        flash('預約成功！', 'success')
        return redirect(url_for('hygiene.my_bookings'))

    return render_template('hygiene/book.html', facility=facility)


@bp.route('/my-bookings')
@login_required
def my_bookings():
    """我的預約"""
    bookings = db.find('hygiene_bookings', user_id=current_user.id)
    bookings.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    
    for booking in bookings:
        fac_id = booking.get('facility_id')
        booking['facility'] = db.get_by_id('hygiene_facilities', fac_id) or {}
    
    return render_template('hygiene/my_bookings.html', bookings=bookings)
