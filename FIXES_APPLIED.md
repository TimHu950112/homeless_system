# 修復記錄 - JSON 遷移後的問題修復

## 概述

本文檔記錄了從 SQLAlchemy 遷移到 JSON 本地存儲後遇到的所有問題及其解決方案。

---

## 修復 #1: 模板字典訪問錯誤

### 問題
```
jinja2.exceptions.UndefinedError: 'str object' has no attribute 'strftime'
```

### 原因
JSON 存儲的數據是字典格式，日期是 ISO 字符串而非 datetime 對象。模板嘗試使用對象屬性訪問方式和 datetime 方法。

### 解決方案

#### 修復的檔案：
1. **app/templates/index.html**
   - 將 `course.start_date.strftime('%Y-%m-%d')` 改為 `course.get('start_date', 'TBD')`
   - 將所有 `object.attribute` 改為 `dict.get('key')`

2. **app/templates/accommodation/index.html**
   - 將 `accommodation.name` 改為 `accommodation.get('name')`
   - 將 `accommodation.target_group` 改為 `accommodation.get('target_group')`
   - 所有欄位改用 `.get()` 方法

3. **app/templates/accommodation/detail.html**
   - 將 `accommodation.name` 改為 `accommodation.get('name')`

4. **app/templates/accommodation/book.html**
   - 將 `accommodation.name` 改為 `accommodation.get('name')`

5. **app/templates/auth/profile.html**
   - 將 `user.created_at.strftime('%Y-%m-%d')` 改為 `user.created_at[:10]`
   - 將 `transaction.created_at.strftime('%Y-%m-%d %H:%M')` 改為 `transaction.get('created_at', '')[:16]`
   - 所有交易記錄欄位改用 `.get()` 方法

---

## 修復 #2: Flask-Login is_active 屬性衝突

### 問題
```
AttributeError: property 'is_active' of 'User' object has no setter
```

### 原因
Flask-Login 的 `UserMixin` 類別已經定義了 `is_active` 作為 property，我們在 `__init__` 中嘗試直接賦值導致衝突。

### 解決方案

**檔案：app/models/user.py**

修改前：
```python
self.is_active = data.get('is_active', True)
```

修改後：
```python
self._is_active = data.get('is_active', True)

@property
def is_active(self):
    """Flask-Login required property"""
    return self._is_active
```

---

## 修復 #3: 缺失的路由端點

### 問題
```
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'courses.detail'
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'food.my_vouchers'
```

### 原因
模板中引用的路由端點在簡化模組中未實現。

### 解決方案

#### 1. **app/routes/courses.py**
新增路由：
```python
@bp.route('/<int:id>')
def detail(id):
    course = db.get_by_id('courses', id)
    return render_template('courses/detail.html', course=course)

@bp.route('/my-courses')
@login_required
def my_courses():
    enrollments = db.find('course_enrollments', user_id=current_user.id)
    return render_template('courses/my_courses.html', enrollments=enrollments)
```

#### 2. **app/routes/employment.py**
新增路由：
```python
@bp.route('/job/<int:id>')
def job_detail(id):
    job = db.get_by_id('jobs', id)
    return render_template('employment/job_detail.html', job=job)

@bp.route('/my-applications')
@login_required
def my_applications():
    applications = db.find('job_applications', user_id=current_user.id)
    return render_template('employment/my_applications.html', applications=applications)
```

#### 3. **app/routes/welfare.py**
新增路由：
```python
@bp.route('/my-applications')
@login_required
def my_applications():
    applications = db.find('welfare_applications', user_id=current_user.id)
    return render_template('welfare/my_applications.html', applications=applications)
```

#### 4. **app/routes/food.py**
新增路由：
```python
@bp.route('/my-vouchers')
@login_required
def my_vouchers():
    vouchers = db.find('meal_vouchers', user_id=current_user.id)
    return render_template('food/my_vouchers.html', vouchers=vouchers)
```

---

## 修復結果

### ✅ 已驗證可正常訪問的頁面

1. **首頁** - `http://localhost:5500/` (HTTP 200)
2. **住宿列表** - `http://localhost:5500/accommodation/` (HTTP 200)
3. **登入頁面** - `http://localhost:5500/auth/login` (HTTP 200)
4. **所有導航連結** - 不再出現 BuildError

### ✅ 已修復的功能

1. **用戶認證**
   - 登入功能正常
   - 註冊功能正常
   - 個人資料頁面可正常顯示

2. **住宿服務**
   - 列表頁面正常顯示
   - 篩選功能正常
   - 預約功能可使用
   - 我的預約頁面正常

3. **導航選單**
   - 所有模組連結正常
   - 用戶下拉選單所有連結正常
   - 不再出現路由錯誤

---

## 技術要點總結

### JSON 數據訪問模式

**模板中：**
```jinja2
<!-- 錯誤 -->
{{ object.attribute }}
{{ object.date.strftime('%Y-%m-%d') }}

<!-- 正確 -->
{{ dict.get('key') }}
{{ dict.get('date', '')[:10] }}
```

**Python 中：**
```python
# User 類別屬性可直接訪問
user.username
user.points

# 但從數據庫返回的字典需要用 .get()
data = db.get_by_id('collection', id)
name = data.get('name')
```

### Flask-Login 屬性處理

UserMixin 提供的屬性：
- `is_active` - 需要作為 property
- `is_authenticated` - 自動提供
- `is_anonymous` - 自動提供
- `get_id()` - 自動提供

如需自定義 `is_active`，必須使用 property 裝飾器。

### 路由命名規範

- 詳情頁：`<module>.detail` 或 `<module>.<item>_detail`
- 個人記錄：`<module>.my_<items>`
- 操作動作：`<module>.<action>_<item>`

---

## 遺留問題

### 未完全實現的功能

以下模組只有列表頁面，詳細功能需要進一步開發：

1. **餐食服務** - 需要實現餐券系統
2. **課程教育** - 需要實現報名和簽到功能
3. **醫療健康** - 需要實現預約和記錄功能
4. **就業培力** - 需要實現申請流程
5. **福利補助** - 需要實現申請和審核流程

### 缺失的模板頁面

雖然路由已創建，但以下模板可能需要完善內容：
- `courses/detail.html`
- `courses/my_courses.html`
- `employment/job_detail.html`
- `employment/my_applications.html`
- `welfare/my_applications.html`
- `food/my_vouchers.html`

---

## 測試建議

### 基本功能測試

1. **註冊與登入**
   ```
   訪問：http://localhost:5500/auth/register
   創建新帳號並登入
   ```

2. **瀏覽服務**
   ```
   首頁：查看統計資訊
   住宿：瀏覽並預約
   其他模組：確認列表可正常顯示
   ```

3. **個人功能**
   ```
   個人資料：查看點數和交易記錄
   我的預約：查看住宿預約記錄
   ```

### 錯誤處理測試

1. **無效路由**
   ```
   訪問不存在的頁面應顯示 404
   ```

2. **未登入保護**
   ```
   未登入時訪問個人頁面應重定向到登入頁
   ```

---

## 維護建議

### 代碼審查清單

修改模板時檢查：
- [ ] 使用 `.get()` 方法訪問字典
- [ ] 日期使用字符串切片而非 strftime
- [ ] url_for 引用的端點已定義

添加新路由時檢查：
- [ ] 路由函數已定義
- [ ] 對應模板已創建
- [ ] 需要的數據已傳遞

修改 User 模型時：
- [ ] 不要直接設置 Flask-Login 的保留屬性
- [ ] 使用 property 裝飾器處理特殊屬性

### 性能優化建議

當前 JSON 存儲適合：
- 開發和測試環境
- 單用戶或小規模使用
- 數據量小於 10MB

如需生產環境部署，建議：
- 遷移至 PostgreSQL 或 MySQL
- 添加數據庫連接池
- 實現緩存機制

---

**修復完成日期：** 2025-10-16
**Flask 版本：** 3.0.0
**Python 版本：** 3.13
