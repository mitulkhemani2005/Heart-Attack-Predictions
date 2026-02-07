from fastapi import FastAPI
from src.data.data_ingestion import data_read
from src.data.data_process import data_process
from src.data.data_transform import data_transform_train
from src.model.model_train import xgb_train
from src.model.basemodel import InputQuestion
from src.model.model_predict import predict_output

app = FastAPI()

@app.get('/')
def home():
    return ({'message': 'Working'})

@app.post('/predict')
def predict(data: InputQuestion):
    y_pred = predict_output(data)
    return ({"message": f"Predicted_value: {y_pred}"})




"""
#Data Related API
@app.get('/data_read')
def data_in ():
    df = data_read()
    if df is not None:
        return ({"message": "Success"})
    return ({"message": "Failed"})

@app.get('/data_process')
def data_prc ():
    df = data_process()
    if df is not None:
        return ({"message": "Success"})
    return ({"message": "Failed"})

@app.get('/data_transform')
def data_trf ():
    X_train_ct, X_test_ct, y_train, y_test = data_transform_train()
    if X_train_ct is not None:
        return ({"message": "Success"})
    return ({"message": "Failed"})
"""

"""
#Model Related API
@app.get('/model_train')
def model_train ():
    model = xgb_train()
    return ({"message": "Model Train"})
"""

