```markdown
# 📘 Stock Price Forecasting + RSI-Based Trading Simulation

This project trains a **time-series forecasting model** (Random Forest Regression) to predict the next-day stock price using historical price inputs.  
After training, the system evaluates the model inside a **rule-based RSI trading strategy**, where:

- **RSI ≥ 70 → Sell ONE stock**
- **RSI ≤ 30 → Buy ONE stock**
- **30 < RSI < 70 → Hold**
- **Cannot hold for more than 5 consecutive days**
- **Only one trade (buy/sell) is allowed per day**

The project visualizes prediction performance and trading behavior (examples shown in the charts you provided).

---

## 📂 Project Structure and File Descriptions

```

├── main.py
├── random_forest_train.py
├── random_forest_test.py
├── random_forest_use.py
├── random_forest_utils.py
├── trading_no_fee.py
├── trading_with_fee.py
├── trading_test.py
├── data_visualization.py
├── utils.py
├── rf_model.pkl
├── Pro3_Data_Stage1.xlsx
├── Pro3_Data_Stage2.xlsx

````

### **Python Files**
- **main.py**  
  Full pipeline: trains RF model, evaluates prediction accuracy, runs RSI-based trading simulations (with & without fees), and plots results.

- **random_forest_train.py**  
  Loads data, engineers features, trains the Random Forest regressor, and saves `rf_model.pkl`.

- **random_forest_test.py**  
  Tests the trained model on held-out data and prints evaluation metrics.

- **random_forest_use.py**  
  Provides a clean function `predict_next_price()` to predict the next value from 10 past prices.

- **random_forest_utils.py**  
  Helper utilities for scaling, metrics, prediction processing, and visualization.

- **trading_no_fee.py / trading_with_fee.py**  
  Executes the RSI-based strategy under two scenarios: no transaction fee vs. fixed transaction fee.

- **trading_test.py**  
  Runs trading logic independently for debugging.

- **data_visualization.py**  
  Centralized plotting utilities.

- **utils.py**  
  General-purpose helper functions (loading Excel, preprocessing, RSI calculation, etc.).

### **Data Files**
- **Pro3_Data_Stage1.xlsx / Pro3_Data_Stage2.xlsx**  
  Original datasets used for feature building and model training.

- **rf_model.pkl**  
  Saved Random Forest model used for inference.

---

## 🚀 How to Use

### 1. Install Dependencies
```bash
pip install -r requirements.txt
````

### 2. Run the full project (train + trade + plots)

```bash
python main.py
```

This will:

* Train a Random Forest forecasting model
* Save `rf_model.pkl`
* Run RSI trading simulation (with and without fees)
* Generate multiple plots (predictions, trading actions, portfolio value)

---

## 📤 Expected Output

Running `main.py` produces:

### **Model Training Metrics**

Example:

```
MSE: 8.4834
RMSE: 2.9126
R2 Score: 0.7704
Model saved to rf_model.pkl
```

### **Trading Simulation Results**

Example:

```
[NO FEE RESULTS]
Final Portfolio Value: 10692.83
Cash Balance: 9787.91
Stocks Owned: 15

[WITH FEE RESULTS]
Final Portfolio Value: 10633.63
Cash Balance: 9728.71
Stocks Owned: 15
```

### **Plots (as shown in your screenshots)**

* Prediction vs. Actual Prices
* Feature Importance
* RSI Strategy Trading Actions
* Portfolio Value Over Time

These generated figures look like:

* Buy = green
* Sell = red
* Hold = blue
* Portfolio value = black line

---

## 🧾 Example: Predicting the Next Price

Use this snippet anywhere after training:

```python
from random_forest_use import predict_next_price

# your 10 input prices
input_prices = [23.7, 25.6, 22.2, 22.3, 22.6, 25.4, 24.5, 26.8, 25.9, 27.8]

# predict 11th price
predicted_price = predict_next_price(input_prices, model_path="rf_model.pkl")

print("Predicted 11th price:", predicted_price)
```

This will output something like:

```
Predicted 11th price: 28.41
```

---

## 📎 Notes

* This is a simplified demonstration of ML forecasting + trading strategy logic.
* It is NOT intended for real financial use.
* The RSI-based strategy is intentionally simple to visualize how model-driven forecasts interact with rule-based trading.

---

