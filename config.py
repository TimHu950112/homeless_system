import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'homeless_services.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 點數設定
    POINTS_PER_HOUR_WORK = 10
    POINTS_PER_COURSE = 5
    POINTS_PER_VOLUNTEER_HOUR = 8
    POINTS_FOR_DAY_ACCOMMODATION = 20

    # 預約設定
    MAX_BOOKING_DAYS = 30
    BOOKING_REMINDER_HOURS = 24
