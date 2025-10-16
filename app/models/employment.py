from datetime import datetime
from app import db

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    job_type = db.Column(db.String(50))  # temporary, part_time, full_time, public_work, craft

    # 工作內容
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(200))
    address = db.Column(db.String(200))

    # 薪資與福利
    salary_type = db.Column(db.String(20))  # hourly, daily, monthly
    salary_min = db.Column(db.Integer)
    salary_max = db.Column(db.Integer)
    points_reward = db.Column(db.Integer, default=0)  # 完成工作可獲得的點數

    # 雇主資訊
    employer = db.Column(db.String(100))
    contact_phone = db.Column(db.String(20))
    contact_person = db.Column(db.String(50))

    # 名額與期限
    vacancies = db.Column(db.Integer, default=1)
    application_deadline = db.Column(db.Date)
    work_start_date = db.Column(db.Date)
    work_end_date = db.Column(db.Date)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    applications = db.relationship('JobApplication', back_populates='job', lazy='dynamic')

    def __repr__(self):
        return f'<Job {self.title}>'


class JobApplication(db.Model):
    __tablename__ = 'job_applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)

    # 申請資訊
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected, completed

    # 自我介紹與備註
    cover_letter = db.Column(db.Text)
    notes = db.Column(db.Text)

    # 工作完成狀態
    work_completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)
    performance_rating = db.Column(db.Integer)  # 1-5分
    feedback = db.Column(db.Text)

    # 時間戳
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='job_applications')
    job = db.relationship('Job', back_populates='applications')

    def __repr__(self):
        return f'<JobApplication {self.id}>'


class CraftProduct(db.Model):
    """文創與手作產品"""
    __tablename__ = 'craft_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))  # handmade, art, recycled, food

    # 產品資訊
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    price = db.Column(db.Integer, default=0)

    # 製作者（可以是多位無家者共同製作）
    makers = db.Column(db.Text)  # JSON格式存儲製作者ID列表

    # 庫存
    stock_quantity = db.Column(db.Integer, default=0)

    # 銷售狀態
    is_available = db.Column(db.Boolean, default=True)
    total_sold = db.Column(db.Integer, default=0)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<CraftProduct {self.name}>'


class WorkshopSession(db.Model):
    """培力工作坊"""
    __tablename__ = 'workshop_sessions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    workshop_type = db.Column(db.String(50))  # resume_writing, interview_skills, life_skills

    # 工作坊資訊
    description = db.Column(db.Text)
    instructor = db.Column(db.String(100))
    location = db.Column(db.String(200))

    # 時間
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.String(50))
    duration_hours = db.Column(db.Float, default=2.0)

    # 名額與獎勵
    max_participants = db.Column(db.Integer, default=15)
    points_reward = db.Column(db.Integer, default=8)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<WorkshopSession {self.title}>'
