from datetime import datetime
from app import db

class Accommodation(db.Model):
    __tablename__ = 'accommodations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    district = db.Column(db.String(50))  # 行政區

    # 床位資訊
    total_beds = db.Column(db.Integer, default=0)
    available_beds = db.Column(db.Integer, default=0)

    # 設施與服務
    facilities = db.Column(db.Text)  # JSON格式：淋浴、洗衣、餐食等
    target_group = db.Column(db.String(50))  # 男性、女性、家庭、高齡者、身障者等

    # 開放時間
    opening_hours = db.Column(db.String(200))
    check_in_time = db.Column(db.String(50))
    check_out_time = db.Column(db.String(50))

    # 聯絡資訊
    contact_phone = db.Column(db.String(20))
    contact_person = db.Column(db.String(50))

    # 照片與描述
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)

    # 每日點數需求
    points_per_day = db.Column(db.Integer, default=20)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    bookings = db.relationship('AccommodationBooking', back_populates='accommodation', lazy='dynamic')

    def __repr__(self):
        return f'<Accommodation {self.name}>'


class AccommodationBooking(db.Model):
    __tablename__ = 'accommodation_bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodations.id'), nullable=False)

    # 預約資訊
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    nights = db.Column(db.Integer, default=1)

    # 點數使用
    points_used = db.Column(db.Integer, default=0)

    # 床位號碼
    bed_number = db.Column(db.String(10))

    # 狀態
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, checked_in, checked_out, cancelled

    # 備註
    notes = db.Column(db.Text)
    social_worker_notes = db.Column(db.Text)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='accommodation_bookings')
    accommodation = db.relationship('Accommodation', back_populates='bookings')

    def __repr__(self):
        return f'<AccommodationBooking {self.id}>'
