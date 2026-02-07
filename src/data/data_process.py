import pandas as pd
from src.data.data_ingestion import data_read

def data_process ():
    df = data_read()
    df.drop(['Patient ID', 'Country', 'Continent', 'Hemisphere', 'Blood Pressure'], axis=1, inplace=True)
    print('Data Processed')
    return df