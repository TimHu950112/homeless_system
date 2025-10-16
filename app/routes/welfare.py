from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.database import db

bp = Blueprint('welfare', __name__, url_prefix='/welfare')

@bp.route('/')
def index():
    programs = db.find('welfare_programs', is_active=True)
    return render_template('welfare/index.html', programs=programs)

@bp.route('/my-applications')
@login_required
def my_applications():
    applications = db.find('welfare_applications', user_id=current_user.id)
    for application in applications:
        program_id = application.get('program_id')
        application['program'] = db.get_by_id('welfare_programs', program_id) or {}
    return render_template('welfare/my_applications.html', applications=applications)
