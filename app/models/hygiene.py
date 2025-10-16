from datetime import datetime
from app import db

class HygieneFacility(db.Model):
    __tablename__ = 'hygiene_facilities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    district = db.Column(db.String(50))

    # 服務類型
    has_shower = db.Column(db.Boolean, default=True)
    has_laundry = db.Column(db.Boolean, default=True)
    has_toilet = db.Column(db.Boolean, default=True)

    # 設施資訊
    total_shower_rooms = db.Column(db.Integer, default=0)
    total_washing_machines = db.Column(db.Integer, default=0)

    # 分區資訊
    has_male_section = db.Column(db.Boolean, default=True)
    has_female_section = db.Column(db.Boolean, default=True)
    has_accessible_section = db.Column(db.Boolean, default=True)

    # 開放時間
    opening_hours = db.Column(db.String(200))

    # 聯絡資訊
    contact_phone = db.Column(db.String(20))

    # 照片與描述
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    bookings = db.relationship('HygieneBooking', back_populates='facility', lazy='dynamic')

    def __repr__(self):
        return f'<HygieneFacility {self.name}>'


class HygieneBooking(db.Model):
    __tablename__ = 'hygiene_bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('hygiene_facilities.id'), nullable=False)

    # 預約資訊
    booking_date = db.Column(db.Date, nullable=False)
    booking_time = db.Column(db.String(20), nullable=False)  # 如 09:00-10:00
    service_type = db.Column(db.String(20))  # shower, laundry, both

    # 狀態
    status = db.Column(db.String(20), default='confirmed')  # confirmed, completed, cancelled, no_show

    # 備註
    notes = db.Column(db.Text)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='hygiene_bookings')
    facility = db.relationship('HygieneFacility', back_populates='bookings')

    def __repr__(self):
        return f'<HygieneBooking {self.id}>'
