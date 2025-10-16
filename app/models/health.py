from datetime import datetime
from app import db

class HealthProvider(db.Model):
    __tablename__ = 'health_providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    provider_type = db.Column(db.String(50))  # hospital, clinic, mobile_clinic, counseling_center

    # 地址與聯絡
    address = db.Column(db.String(200))
    district = db.Column(db.String(50))
    contact_phone = db.Column(db.String(20))

    # 服務項目
    services = db.Column(db.Text)  # JSON: 一般內科、外科、牙科、心理諮商等

    # 營業時間
    opening_hours = db.Column(db.Text)  # JSON格式

    # 義診資訊
    is_free_clinic = db.Column(db.Boolean, default=False)
    free_clinic_schedule = db.Column(db.Text)  # 義診時間表

    # 照片與描述
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    appointments = db.relationship('HealthAppointment', back_populates='provider', lazy='dynamic')

    def __repr__(self):
        return f'<HealthProvider {self.name}>'


class HealthRecord(db.Model):
    __tablename__ = 'health_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # 就診記錄
    visit_date = db.Column(db.Date, nullable=False)
    provider_name = db.Column(db.String(100))
    diagnosis = db.Column(db.Text)
    treatment = db.Column(db.Text)
    medications = db.Column(db.Text)

    # 追蹤事項
    follow_up_date = db.Column(db.Date)
    follow_up_notes = db.Column(db.Text)

    # 記錄者（社工或醫護人員）
    recorded_by = db.Column(db.String(100))

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='health_records')

    def __repr__(self):
        return f'<HealthRecord {self.id}>'


class HealthAppointment(db.Model):
    __tablename__ = 'health_appointments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('health_providers.id'), nullable=False)

    # 預約資訊
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.String(20))
    service_type = db.Column(db.String(50))  # 看診類型

    # 狀態
    status = db.Column(db.String(20), default='scheduled')  # scheduled, completed, cancelled, no_show

    # 備註
    symptoms = db.Column(db.Text)  # 症狀描述
    notes = db.Column(db.Text)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    provider = db.relationship('HealthProvider', back_populates='appointments')

    def __repr__(self):
        return f'<HealthAppointment {self.id}>'


class CounselingSession(db.Model):
    """心理輔導記錄"""
    __tablename__ = 'counseling_sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # 諮商資訊
    session_date = db.Column(db.Date, nullable=False)
    counselor_name = db.Column(db.String(100))
    session_type = db.Column(db.String(50))  # individual, group, emergency
    is_anonymous = db.Column(db.Boolean, default=False)

    # 記錄（保密）
    session_notes = db.Column(db.Text)
    follow_up_needed = db.Column(db.Boolean, default=False)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CounselingSession {self.id}>'
