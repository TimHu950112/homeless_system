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
            'name': '微光驛站',
            'address': '台北車站地下街Z10出口',
            'district': '中正區',
            'total_beds': 30,
            'available_beds': 12,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '隨時',
            'check_out_time': '彈性',
            'contact_phone': '02-2361-9388',
            'contact_person': '服務台',
            'description': '微光驛站以「隱私」與「自由」為核心理念，採獨立式模組設計，打造簡約且具人性化的生活空間，讓使用者在共享環境中亦能感受專屬的安穩與尊嚴。提供單人空間、自助洗衣設施。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '台北市立圓通安養院附設無家者中途之家',
            'address': '台北市士林區',
            'district': '士林區',
            'total_beds': 40,
            'available_beds': 15,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2831-5751',
            'contact_person': '服務台',
            'description': '提供免費住宿與三餐、配置社工與醫護照顧人力、推動彈性管理，轉型陪伴式服務。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '台北市政府社會局委託弘道老人福利基金會辦理「廣安居街友中途之家」',
            'address': '台北市文山區興隆路四段105巷39號',
            'district': '文山區',
            'total_beds': 35,
            'available_beds': 10,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2934-1700',
            'contact_person': '服務台',
            'description': '安排作息與日常活動，培養生活律度、提供溫溼性安置與避寒服務。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '財團法人昌盛教育基金會附設「街友短期安置中心」',
            'address': '台北市萬華區環河南路二段250巷74弄2號',
            'district': '萬華區',
            'total_beds': 30,
            'available_beds': 8,
            'target_group': '男性',
            'opening_hours': '全天24小時',
            'check_in_time': '15:00',
            'check_out_time': '09:00',
            'contact_phone': '02-2304-0131',
            'contact_person': '服務台',
            'description': '提供短期住宿，協助就業過渡、結合就業諮商與職能培訓、提供生活重建與營隊講座介入。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '社團法人台灣芒草心慈善協會「男性無家者中繼安置據點」',
            'address': '台北市萬華區西園路二段261巷18號',
            'district': '萬華區',
            'total_beds': 25,
            'available_beds': 7,
            'target_group': '男性',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2306-1165',
            'contact_person': '服務台',
            'description': '提供密度住宿、降低人際衝突、由社工陪伴並推行自決公約、連結就業與社福資源，提供離所追蹤。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '社團法人台灣芒草心慈善協會「潭馨園女性無家者中繼安置據點」',
            'address': '台北市萬華區昆明街152巷12弄3號',
            'district': '萬華區',
            'total_beds': 20,
            'available_beds': 6,
            'target_group': '女性',
            'opening_hours': '全天24小時',
            'check_in_time': '15:00',
            'check_out_time': '09:00',
            'contact_phone': '02-2375-2099',
            'contact_person': '服務台',
            'description': '提供女性專用避渡住所與隱私空間、結合心理輔導與生活支持、協助自立且標榜穩定租屋。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '社團法人台灣芒草心慈善協會「友善住宿計畫」',
            'address': '台北市萬華區昆明街141號7樓',
            'district': '萬華區',
            'total_beds': 15,
            'available_beds': 5,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2370-5842',
            'contact_person': '服務台',
            'description': '整合包裹代管與社宅資源、以低租金輔導入住社區、提供社工追蹤與維繫穩定生活。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '社團法人台灣人生百味協會「百味家屋無家者住宿據點」',
            'address': '台北市萬華區康定路173巷22號',
            'district': '萬華區',
            'total_beds': 12,
            'available_beds': 4,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2381-2021',
            'contact_person': '服務台',
            'description': '提供小規模住宿與共用生活設施、入住前評估需求並設定自立目標、審查身分與家庭背景，共同決議生活規範。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '社團法人中華方舟救援服務協會「方圓平安棧夜間中途庇護中心」',
            'address': '台北市士林區德行西路40巷17號',
            'district': '士林區',
            'total_beds': 18,
            'available_beds': 6,
            'target_group': '不限',
            'opening_hours': '18:00-08:00',
            'check_in_time': '18:00',
            'check_out_time': '08:00',
            'contact_phone': '02-2831-5751',
            'contact_person': '服務台',
            'description': '提供夜間住宿與洗浴空間、規劃作息與生活輔導、結合工作培力，協助自立生活。',
            'points_per_day': 0,
            'is_active': True
        },
        {
            'name': '財團法人佛教慈濟慈善事業基金會「下一站來來村短期安置中心」',
            'address': '新北市三重區重新路五段609巷59號',
            'district': '三重區',
            'total_beds': 25,
            'available_beds': 8,
            'target_group': '不限',
            'opening_hours': '全天24小時',
            'check_in_time': '14:00',
            'check_out_time': '10:00',
            'contact_phone': '02-2999-8100',
            'contact_person': '服務台',
            'description': '與NGO合作整合跨域資源、提供庇護式短期安置與餐飲服務、協助身心修復並重建生活動態。',
            'points_per_day': 0,
            'is_active': True
        }
    ]

    for accommodation in accommodations:
        db.insert('accommodations', accommodation)

    # 創建盥洗設施
    hygiene_facilities = [
        {
            'name': '微光驛站',
            'address': '台北車站地下街Z10出口',
            'district': '中正區',
            'has_shower': True,
            'has_laundry': True,
            'shower_rooms': 8,
            'washing_machines': 4,
            'has_dryer': True,
            'provides_toiletries': True,
            'service_hours': '全天24小時',
            'contact_phone': '02-2361-9388',
            'description': '微光驛站以「隱私」與「自由」為核心理念，採獨立式模組設計，打造簡約且具人性化的生活空間，讓使用者在共享環境中亦能感受專屬的安穩與尊嚴。提供單人空間、自助洗衣設施。',
            'cost_per_use': 0,
            'is_active': True
        },
        {
            'name': '社團法人台灣芒草心慈善協會「香香澡堂街友盥洗據點」',
            'address': '台北市萬華區昆明街141號',
            'district': '萬華區',
            'has_shower': True,
            'has_laundry': True,
            'shower_rooms': 6,
            'washing_machines': 3,
            'has_dryer': True,
            'provides_toiletries': True,
            'service_hours': '週一至週日 10:00-18:00',
            'contact_phone': '02-2370-5842',
            'description': '提供街友免費盥洗服務，包含淋浴、洗衣、理髮等服務，營造溫馨舒適的盥洗環境，協助街友維持個人衛生與尊嚴。',
            'cost_per_use': 0,
            'is_active': True
        }
    ]

    for facility in hygiene_facilities:
        db.insert('hygiene_facilities', facility)

    # 創建餐食供應點
    food_providers = [
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
            'title': '街遊與體驗營推廣倡議',
            'category': 'advocacy',
            'instructor': '芒草心團隊',
            'organizer': '社團法人台灣芒草心慈善協會',
            'description': '辦理街遊與體驗營推廣倡議、出版街友生命故事，翻轉刻板印象、與校園合作導入DFC教育法。透過實際體驗與故事分享，促進社會理解與包容。',
            'start_date': (today + timedelta(days=14)).date().isoformat(),
            'end_date': (today + timedelta(days=44)).date().isoformat(),
            'schedule': '每週六 10:00-16:00',
            'location': '萬華區',
            'address': '台北市萬華區昆明街141號',
            'max_participants': 20,
            'enrolled_count': 5,
            'delivery_mode': 'in_person',
            'completion_points': 40,
            'attendance_requirement': 0.8,
            'is_active': True
        },
        {
            'title': '社會議題教育推廣',
            'category': 'education',
            'instructor': '人生百味團隊',
            'organizer': '社團法人台灣人生百味協會',
            'description': '在教育場域推出貧窮議題教案、舉辦街頭居牙與共餐活動、開發議題桌遊教材，提升社會理解。透過多元教育方式，讓更多人認識無家者議題。',
            'start_date': (today + timedelta(days=21)).date().isoformat(),
            'end_date': (today + timedelta(days=51)).date().isoformat(),
            'schedule': '每週三、五 14:00-17:00',
            'location': '大安區',
            'address': '台北市大安區羅斯福路三段283巷14弄10號',
            'max_participants': 25,
            'enrolled_count': 8,
            'delivery_mode': 'in_person',
            'completion_points': 45,
            'attendance_requirement': 0.8,
            'is_active': True
        }
    ]

    for course in courses:
        db.insert('courses', course)

    # 創建醫療機構
    health_providers = [
        {
            'name': '台北市立聯合醫院',
            'provider_type': 'hospital',
            'address': '台北市中正區中華路二段33號',
            'district': '中正區',
            'contact_phone': '02-2555-3000',
            'services': '提供免費健檢與醫療補助、設有社工轉介機制協助就醫、松德院區提供心理與精神醫療',
            'opening_hours': '{"weekday": "08:00-17:00", "saturday": "08:00-12:00"}',
            'is_free_clinic': True,
            'description': '提供無家者專屬醫療服務，包含免費健檢、醫療補助、社工協助與精神醫療。',
            'is_active': True
        },
        {
            'name': '國軍北投醫院附設心理衛生中心',
            'provider_type': 'mental_health',
            'address': '台北市北投區新民路60號',
            'district': '北投區',
            'contact_phone': '02-2895-9808',
            'services': '提供壓力諮商與心理治療、執行心理輔導與衛生教育課程、推動傷健障礙外展與轉介',
            'opening_hours': '{"weekday": "08:00-17:00"}',
            'is_free_clinic': True,
            'description': '專注於心理健康服務，提供壓力諮商、心理治療與衛生教育。',
            'is_active': True
        },
        {
            'name': '社團法人台灣俠醫會',
            'provider_type': 'ngo_clinic',
            'address': '台北市萬華區桂林路128號',
            'district': '萬華區',
            'contact_phone': '02-2370-8901',
            'services': '出隊義診與初級醫療服務、提供多科別醫療諮詢、結合醫療與心理陪伴關懷',
            'opening_hours': '{"weekday": "09:00-17:00", "saturday": "09:00-12:00"}',
            'is_free_clinic': True,
            'description': '提供出隊義診服務，結合多科別醫療與心理關懷。',
            'is_active': True
        },
        {
            'name': '財團法人台北市恩友愛心協會',
            'provider_type': 'ngo_health',
            'address': '台北市萬華區環河南路二段250巷74弄2號',
            'district': '萬華區',
            'contact_phone': '02-2304-0131',
            'services': '發放處友卡，在聯盟診所免費就醫、提供心靈重建與信仰輔導、整合探訪與醫療轉介服務',
            'opening_hours': '{"weekday": "09:00-18:00"}',
            'is_free_clinic': True,
            'description': '發放友卡提供免費醫療，結合心靈重建與信仰輔導服務。',
            'is_active': True
        }
    ]

    for provider in health_providers:
        db.insert('health_providers', provider)

    # 創建工作機會
    jobs = [
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

    # 創建示例餐券
    meal_vouchers = [
        {
            'user_id': 1,  # user1
            'meal_type': '午餐',
            'issued_date': today.isoformat(),
            'expiry_date': (today + timedelta(days=30)).isoformat(),
            'is_used': False,
            'used_date': None,
            'provider_name': None,
            'created_at': today.isoformat(),
            'updated_at': today.isoformat()
        },
        {
            'user_id': 1,  # user1
            'meal_type': '晚餐',
            'issued_date': today.isoformat(),
            'expiry_date': (today + timedelta(days=30)).isoformat(),
            'is_used': False,
            'used_date': None,
            'provider_name': None,
            'created_at': today.isoformat(),
            'updated_at': today.isoformat()
        },
        {
            'user_id': 2,  # user2
            'meal_type': '午餐',
            'issued_date': (today - timedelta(days=5)).isoformat(),
            'expiry_date': (today + timedelta(days=25)).isoformat(),
            'is_used': True,
            'used_date': (today - timedelta(days=2)).isoformat(),
            'provider_name': '愛心餐廳 - 大同站',
            'created_at': (today - timedelta(days=5)).isoformat(),
            'updated_at': (today - timedelta(days=2)).isoformat()
        }
    ]

    for voucher in meal_vouchers:
        db.insert('meal_vouchers', voucher)

    print("✓ 示例數據初始化完成！")
    print("\n測試帳號：")
    print("  一般用戶: user1 / password123 (100點, 2張有效餐券)")
    print("  一般用戶: user2 / password123 (50點, 1張已使用餐券)")
    print("  社工: social_worker / password123")
    print("  管理員: admin / admin123")

if __name__ == '__main__':
    init_data()
