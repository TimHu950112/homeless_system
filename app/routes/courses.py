from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.database import db

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('/')
def index():
    courses = db.find('courses', is_active=True)
    return render_template('courses/index.html', courses=courses)

@bp.route('/<int:id>')
def detail(id):
    course = db.get_by_id('courses', id)
    if not course:
        flash('課程不存在', 'danger')
        return redirect(url_for('courses.index'))
    return render_template('courses/detail.html', course=course)

@bp.route('/<int:id>/enroll', methods=['POST'])
@login_required
def enroll(id):
    course = db.get_by_id('courses', id)
    if not course:
        flash('課程不存在', 'danger')
        return redirect(url_for('courses.index'))

    # 檢查是否已報名
    existing = db.find('course_enrollments', user_id=current_user.id, course_id=id)
    if existing:
        flash('您已經報名此課程', 'warning')
        return redirect(url_for('courses.detail', id=id))

    # 檢查名額
    if course.get('enrolled_students', 0) >= course.get('max_students', 0):
        flash('課程名額已滿', 'danger')
        return redirect(url_for('courses.detail', id=id))

    # 創建報名記錄
    enrollment = {
        'user_id': current_user.id,
        'course_id': id,
        'status': 'enrolled',
        'attendance_count': 0
    }
    db.insert('course_enrollments', enrollment)

    # 更新課程已報名人數
    db.update('courses', id, {
        'enrolled_students': course.get('enrolled_students', 0) + 1
    })

    flash('報名成功！', 'success')
    return redirect(url_for('courses.my_courses'))

@bp.route('/my-courses')
@login_required
def my_courses():
    enrollments = db.find('course_enrollments', user_id=current_user.id)
    # 為每個報名添加課程詳情
    for enrollment in enrollments:
        course_id = enrollment.get('course_id')
        enrollment['course'] = db.get_by_id('courses', course_id) or {}
    return render_template('courses/my_courses.html', enrollments=enrollments)
