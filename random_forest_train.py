# random_forest_train.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def create_lag_features(df, window=10):
    df = df.copy()
    for lag in range(1, window + 1):
        df[f'lag_{lag}'] = df['Price'].shift(lag)
    df = df.dropna()
    return df

def train_random_forest(df, model_path="rf_model.pkl"):
    X = df[[f'lag_{i}' for i in range(1, 11)]]
    y = df['Price']

    train_size = int(len(df) * 0.8)
    X_train, y_train = X[:train_size], y[:train_size]

    model = RandomForestRegressor(
        n_estimators=600,
        max_depth=15,
        min_samples_split=20,
        min_samples_leaf=20,
        max_features='log2',
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    return model, X_train, y_train
