# data_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

def visualize_time_series(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], label='Stock Price', linewidth=1.5)
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.show()

def descriptive_stats(df):
    stats = df['Price'].describe().to_frame()
    stats.loc['Skewness'] = df['Price'].skew()
    stats.loc['Kurtosis'] = df['Price'].kurt()
    return stats
