from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.database import db

bp = Blueprint('employment', __name__, url_prefix='/employment')

@bp.route('/')
def index():
    jobs = db.find('jobs', is_active=True)
    return render_template('employment/index.html', jobs=jobs)

@bp.route('/job/<int:id>')
def job_detail(id):
    job = db.get_by_id('jobs', id)
    if not job:
        flash('職缺不存在', 'danger')
        return redirect(url_for('employment.index'))
    return render_template('employment/job_detail.html', job=job)

@bp.route('/job/<int:id>/apply', methods=['POST'])
@login_required
def apply(id):
    job = db.get_by_id('jobs', id)
    if not job:
        flash('職缺不存在', 'danger')
        return redirect(url_for('employment.index'))

    # 檢查是否已申請
    existing = db.find('job_applications', user_id=current_user.id, job_id=id)
    if existing:
        flash('您已經申請過此職缺', 'warning')
        return redirect(url_for('employment.job_detail', id=id))

    # 創建申請記錄
    application = {
        'user_id': current_user.id,
        'job_id': id,
        'status': 'pending'
    }
    db.insert('job_applications', application)

    flash('申請已提交！', 'success')
    return redirect(url_for('employment.my_applications'))

@bp.route('/my-applications')
@login_required
def my_applications():
    applications = db.find('job_applications', user_id=current_user.id)
    for application in applications:
        job_id = application.get('job_id')
        application['job'] = db.get_by_id('jobs', job_id) or {}
    return render_template('employment/my_applications.html', applications=applications)
