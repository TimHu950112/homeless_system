from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.get_by_username(username)

        if user and user.check_password(password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            flash(f'歡迎回來，{user.full_name or user.username}！', 'success')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('帳號或密碼錯誤，請重試。', 'danger')

    return render_template('auth/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        phone = request.form.get('phone')
        gender = request.form.get('gender')

        # 檢查用戶名是否已存在
        if User.get_by_username(username):
            flash('此帳號已被使用，請選擇其他帳號。', 'danger')
            return render_template('auth/register.html')

        # 創建新用戶
        user = User.create(
            username=username,
            password=password,
            full_name=full_name,
            phone=phone,
            gender=gender
        )

        flash('註冊成功！請登入。', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功登出。', 'info')
    return redirect(url_for('main.index'))


@bp.route('/profile')
@login_required
def profile():
    """用戶個人資料頁面"""
    point_transactions = current_user.get_point_transactions(limit=10)

    return render_template('auth/profile.html',
                         user=current_user,
                         point_transactions=point_transactions)


@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """編輯個人資料"""
    if request.method == 'POST':
        updates = {
            'full_name': request.form.get('full_name'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'special_needs': request.form.get('special_needs')
        }
        current_user.update_profile(**updates)
        flash('個人資料已更新。', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/edit_profile.html', user=current_user)
