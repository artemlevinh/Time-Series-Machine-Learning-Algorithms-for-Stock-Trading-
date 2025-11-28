# random_forest_use.py
import numpy as np
import joblib

def predict_next_price(last_10_prices, model_path="rf_model.pkl"):
    model = joblib.load(model_path)
    input_data = np.array(last_10_prices).reshape(1, -1)
    return model.predict(input_data)[0]
