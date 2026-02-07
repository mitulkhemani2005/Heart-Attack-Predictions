from pydantic import BaseModel

class InputQuestion (BaseModel):
    age: int
    sex: str
    cholesterol: int
    heart_rate: int
    diabetes: int
    family_history: int
    smoking: int
    obesity: int
    alcohol_consumption: int
    exercise_hours_per_week: float
    diet: str
    previous_heart_problems: int
    medication_use: int
    stress_level: int
    sedentary_hours_per_day: float
    income: int
    bmi: float
    triglycerides: int
    physical_activity_days_per_week: int
    sleep_hours_per_day: int