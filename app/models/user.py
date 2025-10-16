from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.database import db

class User(UserMixin):
    def __init__(self, data):
        self.data = data
        self.id = data.get('id')
        self.username = data.get('username')
        self.email = data.get('email')
        self.password_hash = data.get('password_hash')
        self.full_name = data.get('full_name')
        self.id_number = data.get('id_number')
        self.phone = data.get('phone')
        self.gender = data.get('gender')
        self.birth_date = data.get('birth_date')
        self.is_disabled = data.get('is_disabled', False)
        self.is_elderly = data.get('is_elderly', False)
        self.special_needs = data.get('special_needs')
        self.user_type = data.get('user_type', 'beneficiary')
        self.points = data.get('points', 0)
        self._is_active = data.get('is_active', True)
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @property
    def is_active(self):
        """Flask-Login required property"""
        return self._is_active

    @staticmethod
    def get_by_id(user_id):
        """根據 ID 獲取用戶"""
        data = db.get_by_id('users', user_id)
        if data:
            return User(data)
        return None

    @staticmethod
    def get_by_username(username):
        """根據用戶名獲取用戶"""
        users = db.find('users', username=username)
        if users:
            return User(users[0])
        return None

    @staticmethod
    def create(username, password, **kwargs):
        """創建新用戶"""
        user_data = {
            'username': username,
            'password_hash': generate_password_hash(password),
            'points': 0,
            'is_active': True,
            'user_type': 'beneficiary',
            **kwargs
        }
        created = db.insert('users', user_data)
        return User(created)

    def check_password(self, password):
        """驗證密碼"""
        return check_password_hash(self.password_hash, password)

    def add_points(self, amount, reason):
        """增加點數"""
        self.points += amount
        db.update('users', self.id, {'points': self.points})

        # 記錄交易
        transaction = {
            'user_id': self.id,
            'amount': amount,
            'transaction_type': 'earn',
            'reason': reason
        }
        db.insert('point_transactions', transaction)

    def deduct_points(self, amount, reason):
        """扣除點數"""
        if self.points >= amount:
            self.points -= amount
            db.update('users', self.id, {'points': self.points})

            # 記錄交易
            transaction = {
                'user_id': self.id,
                'amount': -amount,
                'transaction_type': 'spend',
                'reason': reason
            }
            db.insert('point_transactions', transaction)
            return True
        return False

    def get_point_transactions(self, limit=10):
        """獲取點數交易記錄"""
        transactions = db.find('point_transactions', user_id=self.id)
        # 按時間倒序排序
        transactions.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        return transactions[:limit]

    def update_profile(self, **updates):
        """更新個人資料"""
        db.update('users', self.id, updates)
        for key, value in updates.items():
            setattr(self, key, value)

    @property
    def accommodation_bookings(self):
        """獲取住宿預約"""
        return db.find('accommodation_bookings', user_id=self.id)

    @property
    def hygiene_bookings(self):
        """獲取盥洗預約"""
        return db.find('hygiene_bookings', user_id=self.id)

    @property
    def meal_vouchers(self):
        """獲取餐券"""
        return db.find('meal_vouchers', user_id=self.id)

    @property
    def course_enrollments(self):
        """獲取課程報名"""
        return db.find('course_enrollments', user_id=self.id)

    @property
    def health_records(self):
        """獲取健康記錄"""
        return db.find('health_records', user_id=self.id)

    @property
    def job_applications(self):
        """獲取工作申請"""
        return db.find('job_applications', user_id=self.id)

    @property
    def welfare_applications(self):
        """獲取福利申請"""
        return db.find('welfare_applications', user_id=self.id)

    def __repr__(self):
        return f'<User {self.username}>'
