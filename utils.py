# utils.py
import pandas as pd

def load_data(path):
    df = pd.read_excel(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df
