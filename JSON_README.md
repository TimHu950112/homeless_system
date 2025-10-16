# 無家者服務整合平台 - JSON 本地存儲版本

## ✨ 特色

- ✅ **無需數據庫**: 使用 JSON 文件本地存儲，無需安裝 PostgreSQL 或 MySQL
- ✅ **自動初始化**: 啟動時自動創建示例數據
- ✅ **簡單部署**: 只需 Flask 和 Flask-Login，依賴極少
- ✅ **易於備份**: 所有數據存儲在 `data/` 目錄，直接複製即可備份

## 🚀 快速開始

### 1. 安裝依賴（使用 Pipenv）

```bash
cd /Users/timtim/Downloads/system/homeless_services
pipenv install
```

### 2. 運行應用

```bash
pipenv run python run.py
```

或

```bash
pipenv shell
python run.py
```

### 3. 訪問網站

打開瀏覽器訪問: **http://localhost:5000**

## 🔑 測試帳號

| 角色 | 帳號 | 密碼 | 點數 |
|------|------|------|------|
| 一般用戶 | user1 | password123 | 100 |
| 一般用戶 | user2 | password123 | 50 |
| 社工 | social_worker | password123 | 0 |
| 管理員 | admin | admin123 | 0 |

## 📁 數據存儲結構

所有數據存儲在 `data/` 目錄下的 JSON 文件中：

```
data/
├── users.json                      # 用戶資料
├── accommodations.json             # 收容所
├── accommodation_bookings.json     # 住宿預約
├── hygiene_facilities.json         # 盥洗設施
├── hygiene_bookings.json           # 盥洗預約
├── food_providers.json             # 餐食供應點
├── meal_vouchers.json              # 餐券
├── food_distributions.json         # 剩食發放
├── courses.json                    # 課程
├── course_enrollments.json         # 課程報名
├── health_providers.json           # 醫療機構
├── health_records.json             # 健康記錄
├── health_appointments.json        # 就診預約
├── jobs.json                       # 工作機會
├── job_applications.json           # 工作申請
├── welfare_programs.json           # 福利計畫
├── welfare_applications.json       # 福利申請
└── point_transactions.json         # 點數交易記錄
```

## 🔄 數據管理

### 重置數據

刪除 `data/` 目錄，重新運行應用即可自動重建示例數據：

```bash
rm -rf data
python run.py
```

### 備份數據

直接複製 `data/` 目錄：

```bash
cp -r data data_backup_$(date +%Y%m%d)
```

### 恢復數據

將備份的目錄重命名為 `data`：

```bash
mv data_backup_20251016 data
```

## 🎯 系統特點

### 自動初始化

首次運行時，系統會自動創建：
- 4個測試用戶
- 3個收容所
- 1個盥洗設施
- 2個餐食供應點
- 2個培訓課程
- 2個醫療機構
- 2個工作機會
- 2個福利計畫

### JSON 數據庫API

系統提供簡潔的數據庫操作API：

```python
from app.database import db

# 獲取所有用戶
users = db.get_all('users')

# 根據 ID 獲取
user = db.get_by_id('users', 1)

# 條件查詢
active_users = db.find('users', is_active=True)

# 插入數據
new_user = db.insert('users', {
    'username': 'newuser',
    'points': 0
})

# 更新數據
db.update('users', 1, {'points': 150})

# 刪除數據
db.delete('users', 1)

# 計數
count = db.count('users', is_active=True)
```

## 📦 依賴

僅需3個Python套件：

```
Flask==3.0.0
Flask-Login==0.6.3
Werkzeug==3.0.1
```

## ⚡ 性能說明

- **適用場景**: 中小型部署（< 10,000 用戶）
- **讀取速度**: 毫秒級
- **寫入速度**: 毫秒級（單個JSON文件）
- **並發支持**: 適合單機部署

## 🔐 安全性

- 密碼使用 Werkzeug 加密存儲
- Flask-Login 管理會話
- 所有敏感數據可加密存儲

## 📝 注意事項

1. **生產環境**: 建議使用真實數據庫（PostgreSQL/MySQL）以獲得更好的性能和並發支持
2. **數據備份**: 定期備份 `data/` 目錄
3. **並發寫入**: JSON 存儲不支持高並發寫入，適合讀多寫少的場景

## 🔄 遷移到數據庫

如需遷移到真實數據庫，可參考原版的 SQLAlchemy 實現：

1. 安裝數據庫依賴: `pipenv install flask-sqlalchemy`
2. 使用 `app/__init___old.py` 和 `app/models/*_old.py` 文件
3. 配置數據庫連接字符串

## 📞 支持

如有問題，請參考：
- `README.md` - 完整項目說明
- `SETUP.md` - 安裝指南
- `PROJECT_SUMMARY.md` - 項目總結

---

**享受簡單的部署體驗！** 🎉
