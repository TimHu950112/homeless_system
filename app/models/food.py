from datetime import datetime
from app import db

class FoodProvider(db.Model):
    __tablename__ = 'food_providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    provider_type = db.Column(db.String(50))  # restaurant, convenience_store, food_bank, charity
    address = db.Column(db.String(200))
    district = db.Column(db.String(50))

    # 供餐資訊
    meal_times = db.Column(db.Text)  # JSON: {breakfast: "07:00-09:00", lunch: "11:30-13:30", dinner: "17:30-19:30"}
    daily_capacity = db.Column(db.Integer, default=0)

    # 聯絡資訊
    contact_phone = db.Column(db.String(20))

    # 照片與描述
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)

    # 是否接受餐券
    accepts_voucher = db.Column(db.Boolean, default=True)

    # 狀態
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    vouchers = db.relationship('MealVoucher', back_populates='provider', lazy='dynamic')

    def __repr__(self):
        return f'<FoodProvider {self.name}>'


class MealVoucher(db.Model):
    __tablename__ = 'meal_vouchers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('food_providers.id'), nullable=True)

    # 餐券資訊
    voucher_code = db.Column(db.String(50), unique=True, nullable=False)
    meal_type = db.Column(db.String(20))  # breakfast, lunch, dinner, snack
    value = db.Column(db.Integer, default=100)  # 餐券面額（台幣）

    # 有效期限
    valid_from = db.Column(db.Date, nullable=False)
    valid_until = db.Column(db.Date, nullable=False)

    # 使用狀態
    is_used = db.Column(db.Boolean, default=False)
    used_at = db.Column(db.DateTime)

    # 時間戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯
    user = db.relationship('User', back_populates='meal_vouchers')
    provider = db.relationship('FoodProvider', back_populates='vouchers')

    def __repr__(self):
        return f'<MealVoucher {self.voucher_code}>'


class FoodDistribution(db.Model):
    """剩食優惠與物資發放記錄"""
    __tablename__ = 'food_distributions'

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('food_providers.id'), nullable=False)

    # 物資資訊
    item_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer, default=0)
    expiry_date = db.Column(db.Date)

    # 發放時間
    distribution_date = db.Column(db.Date, nullable=False)
    distribution_time = db.Column(db.String(50))

    # 狀態
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FoodDistribution {self.item_name}>'
