from src.data.data_transform import data_transform_train
from xgboost import XGBClassifier
import pickle

def xgb_train():
    X_train_ct, X_test_ct, y_train, y_test = data_transform_train()
    xgb = XGBClassifier(
        objective='binary:logistic',
        eval_metric='logloss',
        random_state=42
    ).fit(X_train_ct, y_train)
    with open ('save_model/xgb_model.pkl', 'wb') as f:
        pickle.dump(xgb, f)
    print('Model Trained')
    return xgb