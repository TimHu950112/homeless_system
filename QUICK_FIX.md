# 快速修復指南

由於還有許多路由需要更新以適配 JSON 數據庫，建議您先測試核心功能：

## 已完成的功能模塊

✅ **用戶認證** (`auth.py`)
- 登入
- 註冊
- 個人資料查看與編輯

✅ **首頁** (`main.py`)
- 統計資訊顯示
- 最新課程與工作機會

✅ **住宿服務** (`accommodation.py`)
- 查看收容所列表
- 預約住宿
- 查看我的預約
- 取消預約

✅ **盥洗服務** (`hygiene.py`)
- 查看設施列表
- 預約服務
- 查看我的預約

## 暫未完成的模塊

⏳ 餐食服務 (`food.py`)
⏳ 課程管理 (`courses.py`)
⏳ 醫療服務 (`health.py`)
⏳ 就業服務 (`employment.py`)
⏳ 福利補助 (`welfare.py`)
⏳ 社工後台 (`admin.py`)

## 現在可以測試

```bash
pipenv run python run.py
```

訪問：http://localhost:5000

測試功能：
1. 註冊/登入
2. 查看首頁統計
3. 瀏覽收容所
4. 預約住宿（需要足夠點數）
5. 查看個人資料和點數

## 其他模塊快速修復方案

如需使用其他模塊，請參考 `accommodation.py` 和 `hygiene.py` 的修改模式：

1. 將 `Model.query.xxx` 改為 `db.find('collection_name', **filters)`
2. 將 `db.session.add/commit` 改為 `db.insert/update`
3. 處理字典數據而非對象

