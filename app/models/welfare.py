from datetime import datetime
from app import db

class WelfareProgram(db.Model):
    __tablename__ = 'welfare_programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    program_type = db.Column(db.String(50))  # rent_subsidy, health_insurance, living_allowance, disability_support

    # 計畫資訊
    description = db.Column(db.Text)
    benefits = db.Column(db.Text)  # 補助內容
    amount_min = db.Column(db.Integer)  # 最低補助金額
    amount_max = db.Column(db.Integer)  # 最高補助金額

    # 申請資格
    eligibility_criteria = db.Column(db.Text)  # JSON格式
    required_documents = db.Column(db.Text)  # 所需文件清單（JSON）

    # 主辦單位
    organizer = db.Column(db.String(100))
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(100))

    # 申請期限
    application_start = db.Column(db.Date)
    application_end = db.Column(db.Date)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    applications = db.relationship('WelfareApplication', back_populates='program', lazy='dynamic')

    def __repr__(self):
        return f'<WelfareProgram {self.name}>'


class WelfareApplication(db.Model):
    __tablename__ = 'welfare_applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('welfare_programs.id'), nullable=False)

    # 申請資訊
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    application_number = db.Column(db.String(50), unique=True)  # 申請案號

    # 狀態追蹤
    status = db.Column(db.String(20), default='submitted')  # submitted, under_review, approved, rejected, completed
    status_updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 申請文件
    submitted_documents = db.Column(db.Text)  # JSON格式：文件清單與上傳狀態

    # 審核資訊
    reviewer = db.Column(db.String(100))  # 審核人員
    review_notes = db.Column(db.Text)
    approved_amount = db.Column(db.Integer)  # 核准金額

    # 撥款資訊
    disbursement_date = db.Column(db.Date)
    bank_account = db.Column(db.String(100))  # 加密處理

    # 社工協助記錄
    social_worker_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assistance_notes = db.Column(db.Text)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='welfare_applications', foreign_keys=[user_id])
    program = db.relationship('WelfareProgram', back_populates='applications')

    def __repr__(self):
        return f'<WelfareApplication {self.application_number}>'


class EligibilityCheck(db.Model):
    """福利資格試算記錄"""
    __tablename__ = 'eligibility_checks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # 試算資料
    check_date = db.Column(db.DateTime, default=datetime.utcnow)
    input_data = db.Column(db.Text)  # JSON：收入、家庭狀況等
    eligible_programs = db.Column(db.Text)  # JSON：符合資格的計畫清單

    # 試算結果
    estimated_total_amount = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<EligibilityCheck {self.id}>'
