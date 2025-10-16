from datetime import datetime
from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))  # skill_training, art_craft, life_education, employment_prep

    # 課程資訊
    instructor = db.Column(db.String(100))
    organizer = db.Column(db.String(100))  # 主辦單位
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))

    # 時間與地點
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    schedule = db.Column(db.Text)  # 上課時間表（JSON）
    location = db.Column(db.String(200))
    address = db.Column(db.String(200))

    # 名額限制
    max_participants = db.Column(db.Integer, default=20)
    enrolled_count = db.Column(db.Integer, default=0)

    # 授課方式
    delivery_mode = db.Column(db.String(20), default='in_person')  # in_person, online, hybrid

    # 完課獎勵
    completion_points = db.Column(db.Integer, default=5)
    attendance_requirement = db.Column(db.Float, default=0.8)  # 出席率要求（80%）

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    enrollments = db.relationship('CourseEnrollment', back_populates='course', lazy='dynamic')

    def __repr__(self):
        return f'<Course {self.title}>'


class CourseEnrollment(db.Model):
    __tablename__ = 'course_enrollments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    # 報名資訊
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='enrolled')  # enrolled, completed, dropped, failed

    # 出席記錄
    attendance_count = db.Column(db.Integer, default=0)
    total_sessions = db.Column(db.Integer, default=0)
    attendance_rate = db.Column(db.Float, default=0.0)

    # 完課狀態
    is_completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)
    points_awarded = db.Column(db.Integer, default=0)

    # 備註
    notes = db.Column(db.Text)

    # 關聯
    user = db.relationship('User', back_populates='course_enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    def __repr__(self):
        return f'<CourseEnrollment {self.id}>'


class CourseAttendance(db.Model):
    """課程出席記錄"""
    __tablename__ = 'course_attendance'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('course_enrollments.id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    is_present = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CourseAttendance {self.id}>'
