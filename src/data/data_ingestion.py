import pandas as pd

def data_read (file_name = './dataset/heart_attack_prediction_dataset.csv'):
    df = pd.read_csv(file_name)
    print('File Loaded')
    return df