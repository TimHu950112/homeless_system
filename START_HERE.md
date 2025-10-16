# 🚀 開始使用無家者服務整合平台

## ✅ 系統已改為 JSON 本地存儲！

無需數據庫配置，數據自動初始化，立即可用！

## 📦 安裝與啟動

### 方法 1：使用 Pipenv（推薦）

```bash
cd /Users/timtim/Downloads/system/homeless_services

# 安裝依賴
pipenv install

# 運行應用
pipenv run python run.py
```

### 方法 2：不使用 Pipenv

```bash
cd /Users/timtim/Downloads/system/homeless_services

# 安裝依賴
pip install Flask==3.0.0 Flask-Login==0.6.3 Werkzeug==3.0.1

# 運行應用
python run.py
```

## 🌐 訪問網站

啟動後，打開瀏覽器訪問：

**http://localhost:5500**

## 🔑 測試帳號

| 角色 | 帳號 | 密碼 | 點數 |
|------|------|------|------|
| 一般用戶 | user1 | password123 | 100 |
| 一般用戶 | user2 | password123 | 50 |
| 社工 | social_worker | password123 | 0 |
| 管理員 | admin | admin123 | 0 |

## ✨ 已完成功能

### ✅ 核心功能（可直接使用）

1. **用戶認證**
   - 註冊新帳號
   - 登入/登出
   - 個人資料管理
   - 點數查詢

2. **首頁**
   - 服務統計
   - 最新課程展示
   - 最新工作機會

3. **住宿服務**
   - 瀏覽收容所列表
   - 依行政區、族群篩選
   - 預約住宿
   - 查看我的預約
   - 取消預約

4. **盥洗服務**
   - 瀏覽設施列表
   - 預約服務
   - 查看我的預約

### ⏳ 簡化功能（頁面可訪問）

5. **餐食服務** - 列表頁面
6. **課程教育** - 列表頁面
7. **醫療健康** - 列表頁面
8. **就業培力** - 列表頁面
9. **福利補助** - 列表頁面
10. **社工後台** - 基礎頁面

## 📁 數據存儲

所有數據存儲在 `data/` 目錄的 JSON 文件中：

```
data/
├── users.json                      # 用戶資料
├── accommodations.json             # 收容所（3個）
├── hygiene_facilities.json         # 盥洗設施（1個）
├── food_providers.json             # 餐食供應點（2個）
├── courses.json                    # 課程（2個）
├── health_providers.json           # 醫療機構（2個）
├── jobs.json                       # 工作機會（2個）
├── welfare_programs.json           # 福利計畫（2個）
└── ... 其他數據文件
```

## 🔄 數據管理

### 重置所有數據

```bash
rm -rf data/
python run.py  # 會自動重新初始化
```

### 備份數據

```bash
cp -r data/ data_backup_$(date +%Y%m%d)
```

## 🎯 測試流程建議

1. **註冊/登入**
   - 使用 user1 登入（已有100點）

2. **查看首頁**
   - 確認統計資訊正確顯示

3. **瀏覽收容所**
   - 訪問 /accommodation/
   - 嘗試篩選功能

4. **預約住宿**
   - 選擇收容所
   - 填寫入住/退房日期
   - 提交預約（會扣除點數）

5. **查看個人資料**
   - 訪問 /auth/profile
   - 查看點數交易記錄
   - 查看預約記錄

## 📚 相關文檔

- **JSON_README.md** - JSON 存儲詳細說明
- **QUICK_FIX.md** - 功能狀態說明
- **PROJECT_SUMMARY.md** - 完整項目總結

## ❗ 注意事項

1. **首次啟動** - 會自動創建 `data/` 目錄和示例數據
2. **數據持久化** - 所有操作會實時保存到 JSON 文件
3. **並發限制** - JSON 存儲適合單用戶/小規模測試
4. **生產環境** - 建議改用 PostgreSQL/MySQL

## 🆘 遇到問題？

### 問題：ModuleNotFoundError

**解決方案：**
```bash
pipenv install  # 或 pip install -r requirements.txt
```

### 問題：端口被占用

**解決方案：**
修改 `run.py` 中的 port 參數（第20行）

### 問題：數據丟失

**解決方案：**
刪除 `data/` 目錄，重新運行應用即可重建

---

**祝您使用愉快！** 🎉

如有任何問題，請查看相關文檔或聯繫開發團隊。
