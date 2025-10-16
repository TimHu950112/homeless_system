from app import create_app, db
from app.models import *

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Accommodation': Accommodation,
        'AccommodationBooking': AccommodationBooking,
        'HygieneFacility': HygieneFacility,
        'HygieneBooking': HygieneBooking,
        'FoodProvider': FoodProvider,
        'MealVoucher': MealVoucher,
        'Course': Course,
        'CourseEnrollment': CourseEnrollment,
        'HealthProvider': HealthProvider,
        'HealthRecord': HealthRecord,
        'Job': Job,
        'JobApplication': JobApplication,
        'WelfareProgram': WelfareProgram,
        'WelfareApplication': WelfareApplication
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
