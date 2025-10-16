from app.models.user import User

# 為了兼容性，這些類將使用 JSON 數據庫
class Accommodation:
    pass

class FoodProvider:
    pass

class Course:
    pass

class Job:
    pass

class WelfareProgram:
    pass

__all__ = [
    'User',
    'Accommodation',
    'FoodProvider',
    'Course',
    'Job',
    'WelfareProgram'
]
