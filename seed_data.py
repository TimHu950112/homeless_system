"""
示例數據腳本 - 用於初始化數據庫並添加測試數據
運行方式: python seed_data.py
"""

from app import create_app, db
from app.models import *
from datetime import datetime, timedelta

def seed_database():
    app = create_app()

    with app.app_context():
        # 清空現有數據（僅用於開發環境）
        print("清空現有數據...")
        db.drop_all()
        db.create_all()

        # 創建測試用戶
        print("創建測試用戶...")

        # 創建一般受益人用戶
        user1 = User(
            username='user1',
            full_name='王小明',
            phone='0912345678',
            gender='男性',
            user_type='beneficiary',
            points=100
        )
        user1.set_password('password123')

        user2 = User(
            username='user2',
            full_name='李小花',
            phone='0923456789',
            gender='女性',
            user_type='beneficiary',
            points=50
        )
        user2.set_password('password123')

        # 創建社工用戶
        social_worker = User(
            username='social_worker',
            full_name='張社工',
            phone='0934567890',
            user_type='social_worker',
            points=0
        )
        social_worker.set_password('password123')

        # 創建管理員用戶
        admin = User(
            username='admin',
            full_name='系統管理員',
            user_type='admin',
            points=0
        )
        admin.set_password('admin123')

        db.session.add_all([user1, user2, social_worker, admin])
        db.session.commit()

        # 創建收容所
        print("創建收容所數據...")
        accommodation1 = Accommodation(
            name='台北市萬華區緊急庇護所',
            address='台北市萬華區環河南路三段123號',
            district='萬華區',
            total_beds=50,
            available_beds=15,
            target_group='男性',
            opening_hours='全天24小時',
            check_in_time='14:00',
            check_out_time='10:00',
            contact_phone='02-2345-6789',
            contact_person='陳先生',
            description='提供緊急住宿服務，包含基本盥洗設施與餐食。',
            points_per_day=20
        )

        accommodation2 = Accommodation(
            name='新北市板橋女性庇護中心',
            address='新北市板橋區中山路一段456號',
            district='板橋區',
            total_beds=30,
            available_beds=8,
            target_group='女性',
            opening_hours='全天24小時',
            check_in_time='15:00',
            check_out_time='09:00',
            contact_phone='02-8765-4321',
            contact_person='林小姐',
            description='專為女性設計的安全庇護空間，提供心理諮商服務。',
            points_per_day=20
        )

        accommodation3 = Accommodation(
            name='台北市大同區高齡者收容所',
            address='台北市大同區迪化街二段789號',
            district='大同區',
            total_beds=40,
            available_beds=12,
            target_group='高齡者',
            opening_hours='全天24小時',
            check_in_time='13:00',
            check_out_time='11:00',
            contact_phone='02-2555-8888',
            contact_person='黃護理師',
            description='專為高齡無家者設計，提供醫療照護與營養餐食。',
            points_per_day=15
        )

        db.session.add_all([accommodation1, accommodation2, accommodation3])

        # 創建盥洗設施
        print("創建盥洗設施數據...")
        hygiene1 = HygieneFacility(
            name='台北車站盥洗中心',
            address='台北市中正區北平西路3號',
            district='中正區',
            has_shower=True,
            has_laundry=True,
            total_shower_rooms=10,
            total_washing_machines=6,
            has_male_section=True,
            has_female_section=True,
            has_accessible_section=True,
            opening_hours='06:00-22:00',
            contact_phone='02-2311-1234',
            description='提供淋浴、洗衣與基本盥洗用品。'
        )

        db.session.add(hygiene1)

        # 創建餐食供應點
        print("創建餐食供應點數據...")
        food1 = FoodProvider(
            name='慈善廚房 - 萬華站',
            provider_type='charity',
            address='台北市萬華區西園路一段100號',
            district='萬華區',
            meal_times='{"breakfast": "07:00-09:00", "lunch": "11:30-13:30", "dinner": "17:30-19:30"}',
            daily_capacity=200,
            contact_phone='02-2302-5555',
            description='提供免費三餐，無需預約。',
            accepts_voucher=True
        )

        food2 = FoodProvider(
            name='愛心餐廳 - 大同站',
            provider_type='restaurant',
            address='台北市大同區民生西路200號',
            district='大同區',
            meal_times='{"lunch": "11:00-14:00", "dinner": "17:00-20:00"}',
            daily_capacity=100,
            contact_phone='02-2558-7777',
            description='接受電子餐券，提供營養均衡的餐點。',
            accepts_voucher=True
        )

        db.session.add_all([food1, food2])

        # 創建課程
        print("創建課程數據...")
        course1 = Course(
            title='電腦基礎操作班',
            category='skill_training',
            instructor='林老師',
            organizer='台北市勞動力發展局',
            description='學習基本電腦操作，包含文書處理、網路搜尋等技能。',
            start_date=datetime.now().date() + timedelta(days=7),
            end_date=datetime.now().date() + timedelta(days=37),
            schedule='每週一、三、五 14:00-16:00',
            location='台北市職訓中心',
            address='台北市中正區羅斯福路一段4號',
            max_participants=20,
            enrolled_count=5,
            delivery_mode='in_person',
            completion_points=50,
            attendance_requirement=0.8
        )

        course2 = Course(
            title='手作文創工作坊',
            category='art_craft',
            instructor='陳老師',
            organizer='社團法人台北市創意發展協會',
            description='學習各種手工藝技能，製作可販售的文創商品。',
            start_date=datetime.now().date() + timedelta(days=14),
            end_date=datetime.now().date() + timedelta(days=44),
            schedule='每週二、四 10:00-12:00',
            location='萬華社區活動中心',
            address='台北市萬華區昆明街100號',
            max_participants=15,
            enrolled_count=3,
            delivery_mode='in_person',
            completion_points=40,
            attendance_requirement=0.8
        )

        db.session.add_all([course1, course2])

        # 創建醫療機構
        print("創建醫療機構數據...")
        health1 = HealthProvider(
            name='台北市立聯合醫院 - 萬華院區',
            provider_type='hospital',
            address='台北市萬華區內江街87號',
            district='萬華區',
            contact_phone='02-2388-9595',
            services='一般內科、外科、牙科',
            opening_hours='{"weekday": "08:00-17:00", "saturday": "08:00-12:00"}',
            is_free_clinic=False,
            description='提供全方位醫療服務，持健保卡就診。'
        )

        health2 = HealthProvider(
            name='街友健康服務中心',
            provider_type='mobile_clinic',
            address='台北市大同區延平北路二段200號',
            district='大同區',
            contact_phone='02-2550-1234',
            services='基本健康檢查、傷口護理、心理諮商',
            free_clinic_schedule='每週六 09:00-12:00',
            is_free_clinic=True,
            description='提供免費義診服務，不需預約。'
        )

        db.session.add_all([health1, health2])

        # 創建工作機會
        print("創建工作機會數據...")
        job1 = Job(
            title='清潔人員（時薪制）',
            job_type='temporary',
            description='協助環境清潔工作，包含街道、公園等公共空間。',
            requirements='無需經驗，身體健康即可。',
            location='台北市各區',
            address='台北市萬華區',
            salary_type='hourly',
            salary_min=183,
            salary_max=200,
            points_reward=10,
            employer='台北市環保局',
            contact_phone='02-2720-8889',
            vacancies=10,
            application_deadline=datetime.now().date() + timedelta(days=30),
            work_start_date=datetime.now().date() + timedelta(days=7)
        )

        job2 = Job(
            title='餐廳內場助手',
            job_type='part_time',
            description='協助廚房備料、清洗、簡單烹調等工作。',
            requirements='勤奮認真，願意學習。',
            location='台北市大同區',
            address='台北市大同區民生西路100號',
            salary_type='monthly',
            salary_min=28000,
            salary_max=32000,
            points_reward=20,
            employer='愛心餐廳',
            contact_phone='02-2555-6666',
            vacancies=2,
            application_deadline=datetime.now().date() + timedelta(days=14)
        )

        db.session.add_all([job1, job2])

        # 創建福利計畫
        print("創建福利補助計畫數據...")
        welfare1 = WelfareProgram(
            name='租金補助計畫',
            program_type='rent_subsidy',
            description='協助經濟弱勢族群支付租金，減輕居住負擔。',
            benefits='每月補助租金3,000-6,000元',
            amount_min=3000,
            amount_max=6000,
            eligibility_criteria='需符合低收入戶或中低收入戶資格',
            required_documents='身分證、戶籍謄本、租賃契約、財產證明',
            organizer='台北市社會局',
            contact_phone='1999',
            contact_email='welfare@taipei.gov.tw',
            application_start=datetime.now().date(),
            application_end=datetime.now().date() + timedelta(days=90)
        )

        welfare2 = WelfareProgram(
            name='健保費補助',
            program_type='health_insurance',
            description='補助健保費用，確保醫療權益。',
            benefits='全額或部分補助健保費',
            amount_min=800,
            amount_max=1400,
            eligibility_criteria='低收入戶、中低收入戶',
            required_documents='身分證、戶籍謄本、收入證明',
            organizer='衛生福利部',
            contact_phone='1999',
            contact_email='nhi@mohw.gov.tw',
            application_start=datetime.now().date(),
            application_end=datetime.now().date() + timedelta(days=180)
        )

        db.session.add_all([welfare1, welfare2])

        # 提交所有數據
        db.session.commit()

        print("✓ 數據庫初始化完成！")
        print("\n測試帳號：")
        print("  一般用戶: user1 / password123 (100點)")
        print("  一般用戶: user2 / password123 (50點)")
        print("  社工: social_worker / password123")
        print("  管理員: admin / admin123")
        print("\n運行應用: python run.py")

if __name__ == '__main__':
    seed_database()
