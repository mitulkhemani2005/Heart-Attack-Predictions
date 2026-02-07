import pickle
from src.model.basemodel import InputQuestion
import pandas as pd

COLUMN_MAPPING = {
    "age": "Age",
    "sex": "Sex",
    "cholesterol": "Cholesterol",
    "heart_rate": "Heart Rate",
    "diabetes": "Diabetes",
    "family_history": "Family History",
    "smoking": "Smoking",
    "obesity": "Obesity",
    "alcohol_consumption": "Alcohol Consumption",
    "exercise_hours_per_week": "Exercise Hours Per Week",
    "diet": "Diet",
    "previous_heart_problems": "Previous Heart Problems",
    "medication_use": "Medication Use",
    "stress_level": "Stress Level",
    "sedentary_hours_per_day": "Sedentary Hours Per Day",
    "income": "Income",
    "bmi": "BMI",
    "triglycerides": "Triglycerides",
    "physical_activity_days_per_week": "Physical Activity Days Per Week",
    "sleep_hours_per_day": "Sleep Hours Per Day"
}

def predict_output (data: InputQuestion):
    model = None
    standard_transform = None
    with open ('save_model/xgb_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open ('save_model/transform.pkl', 'rb') as f:
        standard_transform = pickle.load(f)

    data = pd.DataFrame([data.dict()])
    data.rename (columns = COLUMN_MAPPING, inplace = True)
    data_trans = standard_transform.transform(data)
    y_pred = model.predict(data_trans)
    print("Value Predicted")
    return y_pred
    