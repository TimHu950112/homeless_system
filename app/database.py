"""
JSON 數據庫管理模組
使用 JSON 文件作為本地數據存儲
"""
import json
import os
from datetime import datetime
from pathlib import Path

class JSONDatabase:
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

        # 定義所有數據文件
        self.files = {
            'users': self.data_dir / 'users.json',
            'accommodations': self.data_dir / 'accommodations.json',
            'accommodation_bookings': self.data_dir / 'accommodation_bookings.json',
            'hygiene_facilities': self.data_dir / 'hygiene_facilities.json',
            'hygiene_bookings': self.data_dir / 'hygiene_bookings.json',
            'food_providers': self.data_dir / 'food_providers.json',
            'meal_vouchers': self.data_dir / 'meal_vouchers.json',
            'food_distributions': self.data_dir / 'food_distributions.json',
            'courses': self.data_dir / 'courses.json',
            'course_enrollments': self.data_dir / 'course_enrollments.json',
            'health_providers': self.data_dir / 'health_providers.json',
            'health_records': self.data_dir / 'health_records.json',
            'health_appointments': self.data_dir / 'health_appointments.json',
            'jobs': self.data_dir / 'jobs.json',
            'job_applications': self.data_dir / 'job_applications.json',
            'welfare_programs': self.data_dir / 'welfare_programs.json',
            'welfare_applications': self.data_dir / 'welfare_applications.json',
            'point_transactions': self.data_dir / 'point_transactions.json',
        }

        # 初始化所有文件
        self._initialize_files()

    def _initialize_files(self):
        """初始化所有 JSON 文件"""
        for key, filepath in self.files.items():
            if not filepath.exists():
                self._save(filepath, [])

    def _load(self, filepath):
        """讀取 JSON 文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save(self, filepath, data):
        """保存到 JSON 文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    def get_all(self, collection):
        """獲取集合中的所有數據"""
        filepath = self.files.get(collection)
        if not filepath:
            return []
        return self._load(filepath)

    def get_by_id(self, collection, item_id):
        """根據 ID 獲取單個項目"""
        items = self.get_all(collection)
        for item in items:
            if item.get('id') == item_id:
                return item
        return None

    def find(self, collection, **filters):
        """根據條件查找項目"""
        items = self.get_all(collection)
        results = []
        for item in items:
            match = True
            for key, value in filters.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                results.append(item)
        return results

    def insert(self, collection, data):
        """插入新數據"""
        items = self.get_all(collection)

        # 生成新 ID
        if items:
            max_id = max(item.get('id', 0) for item in items)
            data['id'] = max_id + 1
        else:
            data['id'] = 1

        # 添加時間戳
        if 'created_at' not in data:
            data['created_at'] = datetime.now().isoformat()

        items.append(data)
        self._save(self.files[collection], items)
        return data

    def update(self, collection, item_id, updates):
        """更新數據"""
        items = self.get_all(collection)
        updated = False

        for item in items:
            if item.get('id') == item_id:
                item.update(updates)
                item['updated_at'] = datetime.now().isoformat()
                updated = True
                break

        if updated:
            self._save(self.files[collection], items)
        return updated

    def delete(self, collection, item_id):
        """刪除數據"""
        items = self.get_all(collection)
        items = [item for item in items if item.get('id') != item_id]
        self._save(self.files[collection], items)

    def clear_all(self):
        """清空所有數據"""
        for filepath in self.files.values():
            self._save(filepath, [])

    def count(self, collection, **filters):
        """計數"""
        if filters:
            return len(self.find(collection, **filters))
        return len(self.get_all(collection))


# 全局數據庫實例
db = JSONDatabase()
