import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Heart Attack Risk Predictor",
    page_icon="❤️",
    layout="wide"
)

# Professional CSS with JetBrains Mono font
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .stApp {
        background-color: #ffffff;
    }
    
    .main-header {
        border-bottom: 2px solid #000000;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        color: #000000;
        font-weight: 600;
        font-size: 1.8rem;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .main-header p {
        color: #666666;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    
    .section-title {
        color: #000000;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .result-box {
        border: 2px solid #000000;
        padding: 1.5rem;
        text-align: center;
        margin-top: 1rem;
    }
    
    .result-low {
        border-color: #000000;
        background-color: #f8f8f8;
    }
    
    .result-high {
        border-color: #000000;
        background-color: #f0f0f0;
    }
    
    .result-text {
        color: #000000;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    .stButton > button {
        background-color: #000000;
        color: #ffffff;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 0.9rem;
        font-weight: 500;
        border-radius: 0;
        width: 100%;
        transition: all 0.2s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        background-color: #333333;
    }
    
    .stSelectbox > div > div,
    .stNumberInput > div > div > input,
    .stSlider > div > div > div {
        border-radius: 0 !important;
    }
    
    div[data-testid="stNumberInput"] input,
    div[data-testid="stSelectbox"] > div > div {
        border-radius: 0 !important;
        border-color: #cccccc !important;
    }
    
    .footer {
        text-align: center;
        color: #888888;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #e0e0e0;
        font-size: 0.75rem;
    }
    
    label {
        font-size: 0.8rem !important;
        color: #333333 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>Heart Attack Risk Predictor</h1>
    <p>Machine Learning Powered Health Analysis</p>
</div>
""", unsafe_allow_html=True)

# API endpoint
API_URL = "http://204.236.195.21:8000/predict"

# Create form columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section-title">Personal Information</div>', unsafe_allow_html=True)
    
    age = st.number_input("Age", min_value=1, max_value=120, value=45)
    sex = st.selectbox("Sex", options=["Male", "Female"])
    income = st.number_input("Annual Income", min_value=0, max_value=1000000, value=50000, step=1000)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Lifestyle</div>', unsafe_allow_html=True)
    
    diet = st.selectbox("Diet", options=["Healthy", "Average", "Unhealthy"])
    smoking = st.selectbox("Smoking", options=["No", "Yes"])
    alcohol_consumption = st.selectbox("Alcohol Consumption", options=["No", "Yes"])
    obesity = st.selectbox("Obesity", options=["No", "Yes"])

with col2:
    st.markdown('<div class="section-title">Health Metrics</div>', unsafe_allow_html=True)
    
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=500, value=200)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=72)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=0, max_value=1000, value=150)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Physical Activity</div>', unsafe_allow_html=True)
    
    exercise_hours_per_week = st.number_input("Exercise Hours/Week", min_value=0.0, max_value=40.0, value=3.0, step=0.5)
    physical_activity_days_per_week = st.number_input("Active Days/Week", min_value=0, max_value=7, value=3)
    sedentary_hours_per_day = st.number_input("Sedentary Hours/Day", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

with col3:
    st.markdown('<div class="section-title">Medical History</div>', unsafe_allow_html=True)
    
    diabetes = st.selectbox("Diabetes", options=["No", "Yes"])
    family_history = st.selectbox("Family History", options=["No", "Yes"])
    previous_heart_problems = st.selectbox("Previous Heart Problems", options=["No", "Yes"])
    medication_use = st.selectbox("On Medication", options=["No", "Yes"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Other Factors</div>', unsafe_allow_html=True)
    
    stress_level = st.slider("Stress Level", min_value=1, max_value=10, value=5)
    sleep_hours_per_day = st.number_input("Sleep Hours/Day", min_value=0, max_value=24, value=7)

# Convert Yes/No to 1/0
def to_binary(val):
    return 1 if val == "Yes" else 0

# Prediction button
st.markdown("<br>", unsafe_allow_html=True)
predict_button = st.button("PREDICT RISK", use_container_width=True)

if predict_button:
    payload = {
        "age": age,
        "sex": sex,
        "cholesterol": cholesterol,
        "heart_rate": heart_rate,
        "diabetes": to_binary(diabetes),
        "family_history": to_binary(family_history),
        "smoking": to_binary(smoking),
        "obesity": to_binary(obesity),
        "alcohol_consumption": to_binary(alcohol_consumption),
        "exercise_hours_per_week": exercise_hours_per_week,
        "diet": diet,
        "previous_heart_problems": to_binary(previous_heart_problems),
        "medication_use": to_binary(medication_use),
        "stress_level": stress_level,
        "sedentary_hours_per_day": sedentary_hours_per_day,
        "income": income,
        "bmi": bmi,
        "triglycerides": triglycerides,
        "physical_activity_days_per_week": physical_activity_days_per_week,
        "sleep_hours_per_day": sleep_hours_per_day
    }
    
    with st.spinner("Analyzing..."):
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                prediction = result.get("message", "")
                
                if "0" in str(prediction) or "Low" in str(prediction):
                    st.markdown("""
                    <div class="result-box result-low">
                        <div class="result-text">LOW RISK</div>
                        <p style="color: #666; margin-top: 0.5rem; font-size: 0.8rem;">Based on the provided data, you have a lower risk of heart attack.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="result-box result-high">
                        <div class="result-text">ELEVATED RISK</div>
                        <p style="color: #666; margin-top: 0.5rem; font-size: 0.8rem;">Please consult with a healthcare professional.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                st.markdown(f"""
                <div style="text-align: center; margin-top: 1rem; font-size: 0.75rem; color: #888;">
                    API Response: {prediction}
                </div>
                """, unsafe_allow_html=True)
                    
            else:
                st.error(f"Error: API returned status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to API. Ensure FastAPI is running on http://localhost:8000")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
st.markdown("""
<div class="footer">
    <p>DISCLAIMER: This tool is for educational purposes only. Not a substitute for professional medical advice.</p>
    <p style="margin-top: 0.25rem;">Built with Streamlit & FastAPI</p>
</div>
""", unsafe_allow_html=True)
