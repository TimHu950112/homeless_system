from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(256))

    # 個人資料
    full_name = db.Column(db.String(100))
    id_number = db.Column(db.String(20), unique=True)  # 身份證字號（加密處理）
    phone = db.Column(db.String(20))
    gender = db.Column(db.String(10))  # 男性、女性、其他
    birth_date = db.Column(db.Date)

    # 特殊需求標記
    is_disabled = db.Column(db.Boolean, default=False)
    is_elderly = db.Column(db.Boolean, default=False)
    special_needs = db.Column(db.Text)  # 特殊需求說明

    # 用戶類型
    user_type = db.Column(db.String(20), default='beneficiary')  # beneficiary, social_worker, admin

    # 點數系統
    points = db.Column(db.Integer, default=0)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    accommodation_bookings = db.relationship('AccommodationBooking', back_populates='user', lazy='dynamic')
    hygiene_bookings = db.relationship('HygieneBooking', back_populates='user', lazy='dynamic')
    meal_vouchers = db.relationship('MealVoucher', back_populates='user', lazy='dynamic')
    course_enrollments = db.relationship('CourseEnrollment', back_populates='user', lazy='dynamic')
    health_records = db.relationship('HealthRecord', back_populates='user', lazy='dynamic')
    job_applications = db.relationship('JobApplication', back_populates='user', lazy='dynamic')
    welfare_applications = db.relationship('WelfareApplication', back_populates='user', lazy='dynamic')
    point_transactions = db.relationship('PointTransaction', back_populates='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_points(self, amount, reason):
        """增加點數並記錄交易"""
        self.points += amount
        transaction = PointTransaction(
            user_id=self.id,
            amount=amount,
            transaction_type='earn',
            reason=reason
        )
        db.session.add(transaction)
        db.session.commit()

    def deduct_points(self, amount, reason):
        """扣除點數並記錄交易"""
        if self.points >= amount:
            self.points -= amount
            transaction = PointTransaction(
                user_id=self.id,
                amount=-amount,
                transaction_type='spend',
                reason=reason
            )
            db.session.add(transaction)
            db.session.commit()
            return True
        return False

    def __repr__(self):
        return f'<User {self.username}>'


class PointTransaction(db.Model):
    __tablename__ = 'point_transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(20))  # earn, spend
    reason = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='point_transactions')

    def __repr__(self):
        return f'<PointTransaction {self.id}: {self.amount}>'
