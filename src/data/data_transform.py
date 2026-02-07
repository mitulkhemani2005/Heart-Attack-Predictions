from src.data.data_process import data_process
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import pickle

def data_transform_train():
    df = data_process()
    X = df.drop('Heart Attack Risk', axis=1)
    y = df['Heart Attack Risk']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    obj = []
    num = []
    for i in X_train.columns:
        if (X_train[i].dtypes == 'object'):
            obj.append(i)
        else:
            num.append(i)

    ct = ColumnTransformer(transformers=[
        ('ohe', OneHotEncoder(), obj),
        ('ss', StandardScaler(), num)
    ],remainder='drop')
    X_train_ct = ct.fit_transform(X_train)

    try:    
        with open ('./save_model/transform.pkl', 'wb') as f:
            pickle.dump(ct, f)
        print ('Data Transformed')
        X_test_ct = ct.transform(X_test)
        return X_train_ct, X_test_ct, y_train, y_test
    except Exception as e:
        print(e)
        return None, None, None, None