# 無家者服務整合平台

這是一個完整的無家者服務整合平台，使用 Flask 和 Bootstrap 5 開發，提供七大核心功能模塊。

## 功能模塊

### 1. 住宿服務
- 查詢與預約收容所
- 顯示可用床位、設施照片、開放時間
- 具體族群標示（女性、高齡者、身障者等）
- 點數系統：參與工作、培訓或志願服務獲得點數延長住宿期

### 2. 盥洗與洗衣服務
- 顯示盥洗與洗衣服務的位置、開放時間
- 線上預約功能
- 男女分區、女性專用區與無障礙設施

### 3. 餐食與物資
- 電子餐券系統
- 剩食優惠機制
- 顯示每日餐食供應點位置與時間

### 4. 課程與教育
- 顯示課程資訊、師資、開課時間
- 完成課程獲得點數獎勵
- 線上學習與現場參與選項

### 5. 醫療與心理健康
- 合作醫院、診所及義診團隊資訊
- 健康檔案與就診記錄
- 心理輔導服務

### 6. 就業與培力
- 短期臨時工作與公益工作機會
- 文創與手作課程
- 穩定就業媒合服務

### 7. 福利與補助
- 各類補助項目查詢
- 線上試算功能
- 申請進度追蹤

## 技術棧

- **後端**: Flask 3.0
- **數據庫**: SQLite（開發環境）/ PostgreSQL（生產環境）
- **前端**: Bootstrap 5、JavaScript
- **認證**: Flask-Login
- **ORM**: SQLAlchemy

## 安裝與運行

### 1. 安裝依賴

```bash
cd homeless_services
pip install -r requirements.txt
```

### 2. 配置環境變量

複製 `.env.example` 為 `.env` 並修改配置：

```bash
cp .env.example .env
```

### 3. 初始化數據庫並添加示例數據

```bash
python seed_data.py
```

### 4. 運行應用

```bash
python run.py
```

應用將在 http://localhost:5000 啟動

## 測試帳號

初始化數據庫後，可使用以下測試帳號登入：

- **一般用戶**:
  - 帳號: `user1` 密碼: `password123` (100點)
  - 帳號: `user2` 密碼: `password123` (50點)

- **社工**:
  - 帳號: `social_worker` 密碼: `password123`

- **管理員**:
  - 帳號: `admin` 密碼: `admin123`

## 目錄結構

```
homeless_services/
├── app/
│   ├── __init__.py              # 應用初始化
│   ├── models/                  # 數據庫模型
│   │   ├── __init__.py
│   │   ├── user.py             # 用戶模型
│   │   ├── accommodation.py    # 住宿模型
│   │   ├── hygiene.py          # 盥洗服務模型
│   │   ├── food.py             # 餐食服務模型
│   │   ├── course.py           # 課程模型
│   │   ├── health.py           # 醫療服務模型
│   │   ├── employment.py       # 就業服務模型
│   │   └── welfare.py          # 福利補助模型
│   ├── routes/                  # 路由控制器
│   │   ├── __init__.py
│   │   ├── main.py             # 主頁路由
│   │   ├── auth.py             # 認證路由
│   │   ├── accommodation.py    # 住宿路由
│   │   ├── hygiene.py          # 盥洗服務路由
│   │   ├── food.py             # 餐食服務路由
│   │   ├── courses.py          # 課程路由
│   │   ├── health.py           # 醫療服務路由
│   │   ├── employment.py       # 就業服務路由
│   │   ├── welfare.py          # 福利補助路由
│   │   └── admin.py            # 後台管理路由
│   ├── templates/               # HTML 模板
│   │   ├── base.html           # 基礎模板
│   │   ├── index.html          # 首頁
│   │   ├── auth/               # 認證相關模板
│   │   ├── accommodation/      # 住宿相關模板
│   │   └── ...                 # 其他模塊模板
│   └── static/                  # 靜態文件
│       ├── css/
│       │   └── style.css       # 自定義樣式
│       ├── js/
│       │   └── main.js         # 自定義 JavaScript
│       └── images/
├── instance/                    # 實例文件（數據庫等）
├── config.py                    # 配置文件
├── run.py                       # 應用啟動文件
├── seed_data.py                 # 示例數據腳本
├── requirements.txt             # Python 依賴
└── README.md                    # 項目說明

```

## 核心功能

### 點數系統

用戶可通過以下方式獲得點數：
- 參與工作：每小時 10 點
- 完成課程：5-50 點（視課程而定）
- 志願服務：每小時 8 點

點數用途：
- 延長住宿期：每天 20 點
- 兌換物資

### 社工後台

社工和管理員可以：
- 查看所有用戶資料
- 審核住宿預約
- 審核福利申請
- 為用戶增加點數
- 查看統計報表

### 響應式設計

使用 Bootstrap 5 實現完全響應式設計，支持：
- 桌面電腦
- 平板設備
- 手機

## 安全性

- 密碼使用 Werkzeug 加密存儲
- Flask-Login 管理用戶會話
- CSRF 保護
- 角色權限控制

## 未來擴展

- [ ] 實時通知系統
- [ ] 多語言支持
- [ ] 地圖整合（Google Maps API）
- [ ] 行動應用程式
- [ ] 數據分析儀表板
- [ ] 導出報表功能（PDF/Excel）

## 授權

本項目僅供教育與學習使用。

## 聯絡

如有問題或建議，請聯繫開發團隊。
