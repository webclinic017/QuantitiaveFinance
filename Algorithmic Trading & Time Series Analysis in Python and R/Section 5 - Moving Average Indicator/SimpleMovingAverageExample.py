# SMA Implmentation

import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

def construct_signals(data, short_period, long_period):
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
    data['Short SMA'] = data['Price'].rolling(window=short_period).mean()
    data['Long SMA'] = data['Price'].rolling(window=long_period).mean()

def plot_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Stock Price', color='black')
    plt.plot(data['Short SMA'], label='Short MA', color='red')
    plt.plot(data['Long SMA'], label='Long MA', color='blue')
    plt.title('Moving Average (MA) Indicators')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.show()


if __name__ == '__main__':
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime(2020, 1, 1)

    stock_data = download_data('IBM', start_date, end_date)
    # plt.plot(stock_data)
    # plt.show()
    construct_signals(stock_data, 50, 200)
    stock_data = stock_data.dropna()
    print(stock_data)
    plot_data(stock_data)