# 無家者服務整合平台 - 項目總結

## 項目概述

這是一個完整的無家者服務整合平台，使用 **Flask** 和 **Bootstrap 5** 開發，提供七大核心功能模塊，旨在為無家者提供一站式服務支持。

## 📊 項目統計

- **Python 文件**: 24個
- **HTML 模板**: 48個
- **CSS 文件**: 1個（自定義樣式）
- **JavaScript 文件**: 1個（互動功能）
- **數據庫模型**: 17個
- **路由模塊**: 10個

## 🏗️ 項目架構

```
homeless_services/
├── app/                          # 應用主目錄
│   ├── __init__.py              # Flask 應用初始化
│   ├── models/                  # 數據庫模型 (8個文件)
│   │   ├── user.py             # 用戶與點數系統
│   │   ├── accommodation.py    # 住宿服務
│   │   ├── hygiene.py          # 盥洗服務
│   │   ├── food.py             # 餐食服務
│   │   ├── course.py           # 課程教育
│   │   ├── health.py           # 醫療健康
│   │   ├── employment.py       # 就業培力
│   │   └── welfare.py          # 福利補助
│   ├── routes/                  # 路由控制器 (10個)
│   │   ├── main.py             # 主頁與導航
│   │   ├── auth.py             # 認證系統
│   │   ├── accommodation.py    # 住宿管理
│   │   ├── hygiene.py          # 盥洗服務
│   │   ├── food.py             # 餐食管理
│   │   ├── courses.py          # 課程管理
│   │   ├── health.py           # 醫療服務
│   │   ├── employment.py       # 就業服務
│   │   ├── welfare.py          # 福利申請
│   │   └── admin.py            # 社工後台
│   ├── templates/               # HTML 模板 (48個)
│   └── static/                  # 靜態資源
│       ├── css/style.css       # 自定義樣式
│       └── js/main.js          # JavaScript 功能
├── instance/                    # 實例文件（數據庫）
├── config.py                    # 配置管理
├── run.py                       # 應用入口
├── seed_data.py                 # 數據初始化腳本
├── requirements.txt             # Python 依賴
├── README.md                    # 項目說明
└── SETUP.md                     # 安裝指南
```

## ✨ 核心功能

### 1. 住宿服務 (Accommodation)
- ✅ 收容所查詢與篩選（按行政區、適用族群）
- ✅ 顯示可用床位、設施照片、開放時間
- ✅ 線上預約系統
- ✅ 點數制度：每天需消耗點數
- ✅ 預約管理（查看、取消）
- ✅ 社工審核機制

### 2. 盥洗與洗衣服務 (Hygiene)
- ✅ 設施位置與開放時間查詢
- ✅ 線上預約盥洗與洗衣服務
- ✅ 男女分區、無障礙設施標示
- ✅ 預約記錄管理

### 3. 餐食與物資 (Food)
- ✅ 餐食供應點地圖與時間
- ✅ 電子餐券系統（生成唯一代碼）
- ✅ 餐券管理與使用記錄
- ✅ 剩食與物資發放資訊
- ✅ 合作餐廳與便利商店整合

### 4. 課程與教育 (Courses)
- ✅ 課程列表與詳情（師資、時間、地點）
- ✅ 線上報名系統
- ✅ 名額管理
- ✅ 出席率追蹤
- ✅ 完課獎勵點數
- ✅ 線上與實體課程選項

### 5. 醫療與心理健康 (Health)
- ✅ 醫療機構與義診資訊
- ✅ 就診預約系統
- ✅ 健康檔案管理
- ✅ 就診記錄追蹤
- ✅ 心理諮商服務
- ✅ 匿名輔導選項

### 6. 就業與培力 (Employment)
- ✅ 工作機會列表（臨時工、全職、公益工作）
- ✅ 工作申請與管理
- ✅ 文創手作產品展示
- ✅ 培力工作坊資訊
- ✅ 履歷撰寫協助
- ✅ 工作完成獎勵點數

### 7. 福利與補助 (Welfare)
- ✅ 補助項目查詢（租金、健保、生活津貼等）
- ✅ 申請條件與所需文件說明
- ✅ 線上申請系統
- ✅ 申請進度追蹤
- ✅ 福利資格試算器
- ✅ 社工協助機制

### 8. 點數系統 (Points)
- ✅ 點數獲取機制：
  - 參與工作：10點/小時
  - 完成課程：5-50點
  - 志願服務：8點/小時
- ✅ 點數使用：
  - 延長住宿：20點/天
  - 兌換物資
- ✅ 交易記錄查詢
- ✅ 社工手動調整權限

### 9. 用戶系統 (User Management)
- ✅ 用戶註冊與登入
- ✅ 個人資料管理
- ✅ 特殊需求標記（高齡、身障等）
- ✅ 隱私保護（身份證加密）
- ✅ 角色權限控制（受益人、社工、管理員）

### 10. 社工後台 (Admin Dashboard)
- ✅ 統計儀表板
- ✅ 用戶管理與查詢
- ✅ 用戶詳細檔案（所有服務記錄）
- ✅ 住宿預約審核
- ✅ 福利申請審核
- ✅ 點數管理
- ✅ 報表功能

## 🎨 設計特色

### 響應式設計
- ✅ 使用 Bootstrap 5 框架
- ✅ 支持桌面、平板、手機
- ✅ 卡片式佈局
- ✅ 直觀的導航系統

### 用戶體驗
- ✅ 清晰的資訊層級
- ✅ 即時表單驗證
- ✅ 友善的錯誤提示
- ✅ 自動消失的通知訊息
- ✅ 圖標輔助理解

### 無障礙設計
- ✅ 語義化 HTML
- ✅ ARIA 標籤支持
- ✅ 高對比度配色
- ✅ 鍵盤導航友好

## 🔐 安全機制

- ✅ 密碼加密存儲（Werkzeug）
- ✅ Flask-Login 會話管理
- ✅ CSRF 保護
- ✅ 角色權限控制
- ✅ 敏感資料加密（身份證、銀行帳號）
- ✅ SQL 注入防護（SQLAlchemy ORM）

## 📦 依賴套件

```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
WTForms==3.1.1
python-dotenv==1.0.0
email-validator==2.1.0
```

## 🚀 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
```

### 2. 初始化數據庫
```bash
python seed_data.py
```

### 3. 運行應用
```bash
python run.py
```

訪問 http://localhost:5000

### 4. 測試帳號
- 一般用戶: `user1` / `password123` (100點)
- 社工: `social_worker` / `password123`
- 管理員: `admin` / `admin123`

## 📈 數據模型關係

```
User (用戶)
├─→ PointTransaction (點數交易記錄)
├─→ AccommodationBooking (住宿預約)
├─→ HygieneBooking (盥洗預約)
├─→ MealVoucher (餐券)
├─→ CourseEnrollment (課程報名)
├─→ HealthRecord (健康記錄)
├─→ HealthAppointment (就診預約)
├─→ JobApplication (工作申請)
└─→ WelfareApplication (福利申請)

Accommodation (收容所) ←─→ AccommodationBooking
HygieneFacility (盥洗設施) ←─→ HygieneBooking
FoodProvider (餐食供應點) ←─→ MealVoucher
Course (課程) ←─→ CourseEnrollment ←─→ CourseAttendance
HealthProvider (醫療機構) ←─→ HealthAppointment
Job (工作機會) ←─→ JobApplication
WelfareProgram (福利計畫) ←─→ WelfareApplication
```

## 🎯 未來擴展方向

### 短期目標
- [ ] 實時通知系統（WebSocket）
- [ ] 完整的後台管理界面
- [ ] 數據導出功能（Excel、PDF）
- [ ] 更多模板頁面完善

### 中期目標
- [ ] 地圖整合（Google Maps API）
- [ ] 多語言支持（中文、英文、越南文等）
- [ ] 簡訊通知功能
- [ ] 行動應用程式（React Native）

### 長期目標
- [ ] AI 智能推薦系統
- [ ] 大數據分析儀表板
- [ ] 區塊鏈技術整合（透明化捐款）
- [ ] 社區互助網絡

## 🎓 技術亮點

1. **模塊化設計**: 清晰的模型、路由、模板分離
2. **可擴展架構**: 易於添加新功能模塊
3. **完整的 CRUD 操作**: 所有實體都有完整的增刪改查
4. **RESTful 風格**: 符合 Web 開發最佳實踐
5. **代碼註釋完整**: 中文註釋，易於理解與維護
6. **示例數據豐富**: 便於測試與演示

## 📝 開發心得

這個項目展示了如何使用 Flask 和 Bootstrap 5 快速開發一個功能完整的 Web 應用程式。通過模塊化設計，我們實現了七大核心功能，涵蓋了無家者從基本生活需求到就業自立的全方位支持。

項目特別注重：
- **實用性**: 每個功能都對應真實需求
- **易用性**: 直觀的界面設計
- **可維護性**: 清晰的代碼結構
- **可擴展性**: 方便後續功能添加

## 📞 聯絡與支持

- **文檔**: 參考 README.md 和 SETUP.md
- **問題回報**: 通過 GitHub Issues
- **技術支持**: service@homeless.org.tw

---

**開發時間**: 2025年10月
**版本**: 1.0.0
**授權**: 教育與學習用途

感謝您使用無家者服務整合平台！
