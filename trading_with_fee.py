# trading_with_fee.py

import matplotlib.pyplot as plt

def trading_with_fee(y_test, y_pred, rsi_series, df, y_train, fee=0.02):
    initial_cash = 10000
    initial_stocks = 10
    cash_balance = initial_cash
    stocks_owned = initial_stocks

    portfolio_values = [cash_balance + stocks_owned * y_test.iloc[-1]]
    actions = []
    action_counter = {'Buy': 0, 'Sell': 0, 'Hold': 0}
    last_action = None
    max_consecutive_actions = 5

    for i in range(len(y_test)):
        current_price = y_test.iloc[i]
        predicted_price = y_pred[i]
        rsi = rsi_series.iloc[i]

        action = "Hold"

        if rsi < 30 and predicted_price > current_price:
            action = "Buy"
            effective_price = current_price * (1 + fee)
            if cash_balance >= effective_price:
                stocks_owned += 1
                cash_balance -= effective_price

        elif rsi > 70 and predicted_price < current_price and stocks_owned > 0:
            action = "Sell"
            effective_price = current_price * (1 - fee)
            stocks_owned -= 1
            cash_balance += effective_price

        if action == last_action:
            action_counter[action] += 1
            if action_counter[action] > max_consecutive_actions:
                action = "Hold"
        else:
            action_counter = {k: 0 for k in action_counter}
            action_counter[action] = 1

        if action == "Hold" and action_counter["Hold"] > max_consecutive_actions:
            if stocks_owned > 0:
                action = "Sell"
                effective_price = current_price * (1 - fee)
                stocks_owned -= 1
                cash_balance += effective_price

        last_action = action
        actions.append(action)

        portfolio_values.append(cash_balance + stocks_owned * current_price)

    portfolio_values = portfolio_values[1:]
    final_portfolio_value = cash_balance + stocks_owned * y_test.iloc[-1]

    print("\n[WITH FEE RESULTS]")
    print("Final Portfolio Value:", final_portfolio_value)
    print("Cash Balance:", cash_balance)
    print("Stocks Owned:", stocks_owned)

    # Plot 1 (index)
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(y_test.index, portfolio_values, color="black", linewidth=2, label="Portfolio Value")

    ax2 = ax1.twinx()
    buy_idx  = [i for i,a in enumerate(actions) if a=="Buy"]
    sell_idx = [i for i,a in enumerate(actions) if a=="Sell"]
    hold_idx = [i for i,a in enumerate(actions) if a=="Hold"]

    ax2.scatter(buy_idx,  [portfolio_values[i] for i in buy_idx], color="green", label="Buy")
    ax2.scatter(sell_idx, [portfolio_values[i] for i in sell_idx], color="red",   label="Sell")
    ax2.scatter(hold_idx, [portfolio_values[i] for i in hold_idx], color="blue",  label="Hold")

    plt.title("Trading Actions & Portfolio Value (WITH 2% Fee)")
    fig.legend(loc="upper left")
    plt.show()

    # Plot 2 (date)
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot([df['Date'].iloc[len(y_train)+i] for i in range(len(portfolio_values))],
             portfolio_values, color="black", linewidth=2, label="Portfolio Value")

    ax2 = ax1.twinx()
    ax2.scatter([df['Date'].iloc[len(y_train)+i] for i in buy_idx],
                [portfolio_values[i] for i in buy_idx], color="green", label="Buy")
    ax2.scatter([df['Date'].iloc[len(y_train)+i] for i in sell_idx],
                [portfolio_values[i] for i in sell_idx], color="red", label="Sell")
    ax2.scatter([df['Date'].iloc[len(y_train)+i] for i in hold_idx],
                [portfolio_values[i] for i in hold_idx], color="blue", label="Hold")

    plt.title("Trading Actions & Portfolio Value (Dates, WITH 2% Fee)")
    fig.legend(loc="upper left")
    plt.show()

    return portfolio_values, actions, final_portfolio_value
