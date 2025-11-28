# trading_test.py
import pandas as pd
import numpy as np

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def trading_simulation(y_test, y_pred, rsi, transaction_cost=0.0):
    cash = 10000
    stocks = 10
    portfolio_values = []

    for price, pred, r in zip(y_test, y_pred, rsi):
        action = "Hold"

        if r < 30 and pred > price:
            action = "Buy"
            cost = price * (1 + transaction_cost)
            if cash >= cost:
                cash -= cost
                stocks += 1

        elif r > 70 and pred < price and stocks > 0:
            action = "Sell"
            revenue = price * (1 - transaction_cost)
            cash += revenue
            stocks -= 1

        portfolio_values.append(cash + stocks * price)

    final_value = portfolio_values[-1]
    return portfolio_values, final_value
