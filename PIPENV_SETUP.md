# Pipenv 安裝指南

## 使用 Pipenv 安裝與運行

### 1. 安裝依賴

在項目目錄下執行：

```bash
cd /Users/timtim/Downloads/system/homeless_services
pipenv install
```

### 2. 初始化數據庫

```bash
pipenv run python seed_data.py
```

### 3. 運行應用

```bash
pipenv run python run.py
```

或者先進入虛擬環境：

```bash
pipenv shell
python seed_data.py
python run.py
```

## 快速命令參考

```bash
# 安裝依賴
pipenv install

# 進入虛擬環境
pipenv shell

# 在虛擬環境中執行命令
pipenv run python seed_data.py
pipenv run python run.py

# 退出虛擬環境
exit
```

## 測試帳號

- **一般用戶**: `user1` / `password123` (100點)
- **社工**: `social_worker` / `password123`
- **管理員**: `admin` / `admin123`

## 訪問網站

啟動後訪問: http://localhost:5000
