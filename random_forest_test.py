# random_forest_test.py
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import joblib

def test_random_forest(df, model_path="rf_model.pkl"):
    model = joblib.load(model_path)

    X = df[[f'lag_{i}' for i in range(1, 11)]]
    y = df['Price']

    train_size = int(len(df) * 0.8)
    X_test, y_test = X[train_size:], y[train_size:]

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    return y_test, y_pred
