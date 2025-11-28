# main.py

from utils import load_data
from data_visualization import visualize_time_series
from random_forest_train import create_lag_features, train_random_forest
from random_forest_test import test_random_forest
from trading_test import calculate_rsi
from trading_no_fee import trading_no_fee
from trading_with_fee import trading_with_fee

def main():
    df = load_data("Pro3_Data_Stage1.xlsx")

    visualize_time_series(df)

    df_lag = create_lag_features(df)
    model, X_train, y_train = train_random_forest(df_lag)
    y_test, y_pred = test_random_forest(df_lag)

    rsi = calculate_rsi(y_test)

    # --- Trading without fee ---
    trading_no_fee(y_test, y_pred, rsi, df, y_train)

    # --- Trading with 2% fee ---
    trading_with_fee(y_test, y_pred, rsi, df, y_train, fee=0.02)

if __name__ == "__main__":
    main()

