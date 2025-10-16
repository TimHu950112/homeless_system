"""
自動初始化示例數據
"""
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from app.database import db

def init_data():
    """初始化所有示例數據"""

    # 檢查是否已有數據
    if db.count('users') > 0:
        print("數據已存在，跳過初始化")
        return

    print("初始化示例數據...")

    # 清空現有數據
    db.clear_all()

    # 創建用戶
    users = [
        {
            'username': 'user1',
            'password_hash': generate_password_hash('password123'),
            'full_name': '王小明',
            'phone': '0912345678',
            'gender': '男性',
            'user_type': 'beneficiary',
            'points': 100,
            'is_active': True
        },
        {
            'username': 'user2',
            'password_hash': generate_password_hash('password123'),
            'full_name': '李小花',
            'phone': '0923456789',
            'gender': '女性',
            'user_type': 'beneficiary',
            'points': 50,
            'is_active': True
        },
        {
            'username': 'social_worker',
            'password_hash': generate_password_hash('password123'),
            'full_name': '張社工',
            'phone': '0934567890',
            'user_type': 'social_worker',
            'points': 0,
            'is_active': True
        },
        {
            'username': 'admin',
            'password_hash': generate_password_hash('admin123'),
            'full_name': '系統管理員',
            'user_type': 'admin',
            'points': 0,
            'is_active': True
        }
    ]

    for user in users:
        db.insert('users', user)

    # 創建收容所
    accommodations = [
        {
            'name': '台北市萬華區緊急庇護所',
            'address': '台北市萬華區環河南路三段123號',
            'district': '萬華區',
            'total_beds': 50,
            'available_beds': 15,
            'target_group': '男性',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2345-6789',
            'contact_person': '陳先生',
            'description': '提供緊急住宿服務，包含基本盥洗設施與餐食。',
            'points_per_day': 20,
            'is_active': True
        },
        {
            'name': '新北市板橋女性庇護中心',
            'address': '新北市板橋區中山路一段456號',
            'district': '板橋區',
            'total_beds': 30,
            'available_beds': 8,
            'target_group': '女性',
            'opening_hours': '全天24小時',
            'check_in_time': '15:00',
            'check_out_time': '09:00',
            'contact_phone': '02-8765-4321',
            'contact_person': '林小姐',
            'description': '專為女性設計的安全庇護空間，提供心理諮商服務。',
            'points_per_day': 20,
            'is_active': True
        },
        {
            'name': '台北市大同區高齡者收容所',
            'address': '台北市大同區迪化街二段789號',
            'district': '大同區',
            'total_beds': 40,
            'available_beds': 12,
            'target_group': '高齡者',
            'opening_hours': '全天24小時',
            'check_in_time': '13:00',
            'check_out_time': '11:00',
            'contact_phone': '02-2555-8888',
            'contact_person': '黃護理師',
            'description': '專為高齡無家者設計，提供醫療照護與營養餐食。',
            'points_per_day': 15,
            'is_active': True
        }
    ]

    for accommodation in accommodations:
        db.insert('accommodations', accommodation)

    # 創建盥洗設施
    hygiene_facilities = [
        {
            'name': '台北車站盥洗中心',
            'address': '台北市中正區北平西路3號',
            'district': '中正區',
            'has_shower': True,
            'has_laundry': True,
            'total_shower_rooms': 10,
            'total_washing_machines': 6,
            'has_male_section': True,
            'has_female_section': True,
            'has_accessible_section': True,
            'opening_hours': '06:00-22:00',
            'contact_phone': '02-2311-1234',
            'description': '提供淋浴、洗衣與基本盥洗用品。',
            'is_active': True
        }
    ]

    for facility in hygiene_facilities:
        db.insert('hygiene_facilities', facility)

    # 創建餐食供應點
    food_providers = [
        {
            'name': '慈善廚房 - 萬華站',
            'provider_type': 'charity',
            'address': '台北市萬華區西園路一段100號',
            'district': '萬華區',
            'meal_times': '{"breakfast": "07:00-09:00", "lunch": "11:30-13:30", "dinner": "17:30-19:30"}',
            'daily_capacity': 200,
            'contact_phone': '02-2302-5555',
            'description': '提供免費三餐，無需預約。',
            'accepts_voucher': True,
            'is_active': True
        },
        {
            'name': '愛心餐廳 - 大同站',
            'provider_type': 'restaurant',
            'address': '台北市大同區民生西路200號',
            'district': '大同區',
            'meal_times': '{"lunch": "11:00-14:00", "dinner": "17:00-20:00"}',
            'daily_capacity': 100,
            'contact_phone': '02-2558-7777',
            'description': '接受電子餐券，提供營養均衡的餐點。',
            'accepts_voucher': True,
            'is_active': True
        }
    ]

    for provider in food_providers:
        db.insert('food_providers', provider)

    # 創建課程
    today = datetime.now()
    courses = [
        {
            'title': '電腦基礎操作班',
            'category': 'skill_training',
            'instructor': '林老師',
            'organizer': '台北市勞動力發展局',
            'description': '學習基本電腦操作，包含文書處理、網路搜尋等技能。',
            'start_date': (today + timedelta(days=7)).date().isoformat(),
            'end_date': (today + timedelta(days=37)).date().isoformat(),
            'schedule': '每週一、三、五 14:00-16:00',
            'location': '台北市職訓中心',
            'address': '台北市中正區羅斯福路一段4號',
            'max_participants': 20,
            'enrolled_count': 5,
            'delivery_mode': 'in_person',
            'completion_points': 50,
            'attendance_requirement': 0.8,
            'is_active': True
        },
        {
            'title': '手作文創工作坊',
            'category': 'art_craft',
            'instructor': '陳老師',
            'organizer': '社團法人台北市創意發展協會',
            'description': '學習各種手工藝技能，製作可販售的文創商品。',
            'start_date': (today + timedelta(days=14)).date().isoformat(),
            'end_date': (today + timedelta(days=44)).date().isoformat(),
            'schedule': '每週二、四 10:00-12:00',
            'location': '萬華社區活動中心',
            'address': '台北市萬華區昆明街100號',
            'max_participants': 15,
            'enrolled_count': 3,
            'delivery_mode': 'in_person',
            'completion_points': 40,
            'attendance_requirement': 0.8,
            'is_active': True
        }
    ]

    for course in courses:
        db.insert('courses', course)

    # 創建醫療機構
    health_providers = [
        {
            'name': '台北市立聯合醫院 - 萬華院區',
            'provider_type': 'hospital',
            'address': '台北市萬華區內江街87號',
            'district': '萬華區',
            'contact_phone': '02-2388-9595',
            'services': '一般內科、外科、牙科',
            'opening_hours': '{"weekday": "08:00-17:00", "saturday": "08:00-12:00"}',
            'is_free_clinic': False,
            'description': '提供全方位醫療服務，持健保卡就診。',
            'is_active': True
        },
        {
            'name': '街友健康服務中心',
            'provider_type': 'mobile_clinic',
            'address': '台北市大同區延平北路二段200號',
            'district': '大同區',
            'contact_phone': '02-2550-1234',
            'services': '基本健康檢查、傷口護理、心理諮商',
            'free_clinic_schedule': '每週六 09:00-12:00',
            'is_free_clinic': True,
            'description': '提供免費義診服務，不需預約。',
            'is_active': True
        }
    ]

    for provider in health_providers:
        db.insert('health_providers', provider)

    # 創建工作機會
    jobs = [
        {
            'title': '清潔人員（時薪制）',
            'job_type': 'temporary',
            'description': '協助環境清潔工作，包含街道、公園等公共空間。',
            'requirements': '無需經驗，身體健康即可。',
            'location': '台北市各區',
            'address': '台北市萬華區',
            'salary_type': 'hourly',
            'salary_min': 183,
            'salary_max': 200,
            'points_reward': 10,
            'employer': '台北市環保局',
            'contact_phone': '02-2720-8889',
            'vacancies': 10,
            'application_deadline': (today + timedelta(days=30)).date().isoformat(),
            'work_start_date': (today + timedelta(days=7)).date().isoformat(),
            'is_active': True
        },
        {
            'title': '餐廳內場助手',
            'job_type': 'part_time',
            'description': '協助廚房備料、清洗、簡單烹調等工作。',
            'requirements': '勤奮認真，願意學習。',
            'location': '台北市大同區',
            'address': '台北市大同區民生西路100號',
            'salary_type': 'monthly',
            'salary_min': 28000,
            'salary_max': 32000,
            'points_reward': 20,
            'employer': '愛心餐廳',
            'contact_phone': '02-2555-6666',
            'vacancies': 2,
            'application_deadline': (today + timedelta(days=14)).date().isoformat(),
            'is_active': True
        }
    ]

    for job in jobs:
        db.insert('jobs', job)

    # 創建福利計畫
    welfare_programs = [
        {
            'name': '租金補助計畫',
            'program_type': 'rent_subsidy',
            'description': '協助經濟弱勢族群支付租金，減輕居住負擔。',
            'benefits': '每月補助租金3,000-6,000元',
            'amount_min': 3000,
            'amount_max': 6000,
            'eligibility_criteria': '需符合低收入戶或中低收入戶資格',
            'required_documents': '身分證、戶籍謄本、租賃契約、財產證明',
            'organizer': '台北市社會局',
            'contact_phone': '1999',
            'contact_email': 'welfare@taipei.gov.tw',
            'application_start': today.date().isoformat(),
            'application_end': (today + timedelta(days=90)).date().isoformat(),
            'is_active': True
        },
        {
            'name': '健保費補助',
            'program_type': 'health_insurance',
            'description': '補助健保費用，確保醫療權益。',
            'benefits': '全額或部分補助健保費',
            'amount_min': 800,
            'amount_max': 1400,
            'eligibility_criteria': '低收入戶、中低收入戶',
            'required_documents': '身分證、戶籍謄本、收入證明',
            'organizer': '衛生福利部',
            'contact_phone': '1999',
            'contact_email': 'nhi@mohw.gov.tw',
            'application_start': today.date().isoformat(),
            'application_end': (today + timedelta(days=180)).date().isoformat(),
            'is_active': True
        }
    ]

    for program in welfare_programs:
        db.insert('welfare_programs', program)

    print("✓ 示例數據初始化完成！")
    print("\n測試帳號：")
    print("  一般用戶: user1 / password123 (100點)")
    print("  一般用戶: user2 / password123 (50點)")
    print("  社工: social_worker / password123")
    print("  管理員: admin / admin123")

if __name__ == '__main__':
    init_data()
