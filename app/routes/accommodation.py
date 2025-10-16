from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from app.database import db

bp = Blueprint('accommodation', __name__, url_prefix='/accommodation')

@bp.route('/')
def index():
    """住宿列表頁面"""
    # 獲取篩選條件
    district = request.args.get('district', '')
    target_group = request.args.get('target_group', '')

    # 基本查詢
    accommodations = db.find('accommodations', is_active=True)

    # 應用篩選
    if district:
        accommodations = [a for a in accommodations if a.get('district') == district]
    if target_group:
        accommodations = [a for a in accommodations if a.get('target_group') == target_group]

    # 獲取可用的行政區列表
    all_accommodations = db.get_all('accommodations')
    districts = list(set(a.get('district') for a in all_accommodations if a.get('district')))
    districts.sort()

    return render_template('accommodation/index.html',
                         accommodations=accommodations,
                         districts=districts,
                         selected_district=district,
                         selected_target_group=target_group)


@bp.route('/<int:id>')
def detail(id):
    """住宿詳情頁面"""
    accommodation = db.get_by_id('accommodations', id)
    if not accommodation:
        flash('找不到該收容所。', 'danger')
        return redirect(url_for('accommodation.index'))
    return render_template('accommodation/detail.html', accommodation=accommodation)


@bp.route('/<int:id>/book', methods=['GET', 'POST'])
@login_required
def book(id):
    """預約住宿"""
    accommodation = db.get_by_id('accommodations', id)
    if not accommodation:
        flash('找不到該收容所。', 'danger')
        return redirect(url_for('accommodation.index'))

    if request.method == 'POST':
        check_in_date = datetime.strptime(request.form.get('check_in_date'), '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.form.get('check_out_date'), '%Y-%m-%d').date()
        notes = request.form.get('notes', '')

        # 驗證日期
        if check_in_date < datetime.now().date():
            flash('入住日期不能早於今天。', 'danger')
            return redirect(url_for('accommodation.book', id=id))

        if check_out_date <= check_in_date:
            flash('退房日期必須晚於入住日期。', 'danger')
            return redirect(url_for('accommodation.book', id=id))

        # 計算天數和所需點數
        nights = (check_out_date - check_in_date).days
        points_needed = accommodation.get('points_per_day', 20) * nights

        # 檢查點數是否足夠
        if current_user.points < points_needed:
            flash(f'點數不足。您目前有 {current_user.points} 點，需要 {points_needed} 點。', 'danger')
            return redirect(url_for('accommodation.book', id=id))

        # 檢查是否有可用床位
        if accommodation.get('available_beds', 0) < 1:
            flash('抱歉，目前沒有可用床位。', 'danger')
            return redirect(url_for('accommodation.detail', id=id))

        # 創建預約
        booking = {
            'user_id': current_user.id,
            'accommodation_id': accommodation['id'],
            'check_in_date': check_in_date.isoformat(),
            'check_out_date': check_out_date.isoformat(),
            'nights': nights,
            'points_used': points_needed,
            'notes': notes,
            'status': 'pending'
        }

        db.insert('accommodation_bookings', booking)

        flash(f'預約申請已提交！待審核通過後將扣除 {points_needed} 點。', 'success')
        return redirect(url_for('accommodation.my_bookings'))

    return render_template('accommodation/book.html', accommodation=accommodation)


@bp.route('/my-bookings')
@login_required
def my_bookings():
    """我的住宿預約"""
    bookings = db.find('accommodation_bookings', user_id=current_user.id)
    bookings.sort(key=lambda x: x.get('created_at', ''), reverse=True)

    # 添加 accommodation 資訊
    for booking in bookings:
        acc_id = booking.get('accommodation_id')
        booking['accommodation'] = db.get_by_id('accommodations', acc_id) or {}

    return render_template('accommodation/my_bookings.html', bookings=bookings)


@bp.route('/booking/<int:id>/cancel', methods=['POST'])
@login_required
def cancel_booking(id):
    """取消預約"""
    booking = db.get_by_id('accommodation_bookings', id)

    if not booking:
        flash('找不到該預約。', 'danger')
        return redirect(url_for('accommodation.my_bookings'))

    # 驗證是否為本人預約
    if booking.get('user_id') != current_user.id:
        flash('無權限執行此操作。', 'danger')
        return redirect(url_for('accommodation.my_bookings'))

    # 只能取消未開始的預約
    check_in_str = booking.get('check_in_date', '')
    if check_in_str:
        check_in_date = datetime.fromisoformat(check_in_str).date()
        if check_in_date <= datetime.now().date():
            flash('無法取消已開始或過去的預約。', 'danger')
            return redirect(url_for('accommodation.my_bookings'))

    # 如果已確認並扣除點數，需要退還點數
    if booking.get('status') == 'confirmed' and booking.get('points_used', 0) > 0:
        current_user.add_points(booking['points_used'], f'取消住宿預約 #{booking["id"]}')

    db.update('accommodation_bookings', id, {'status': 'cancelled'})

    flash('預約已取消。', 'info')
    return redirect(url_for('accommodation.my_bookings'))
