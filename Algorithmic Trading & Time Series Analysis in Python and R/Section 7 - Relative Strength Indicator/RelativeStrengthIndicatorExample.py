# RSI Implementation

import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['price'] = ticker['Adj Close']
    return pd.DataFrame(data)


if __name__ == '__main__':
    start_date = datetime.datetime(2015, 1, 1)
    end_date = datetime.datetime(2020, 1, 1)

    stock_data = download_data('IBM', start_date, end_date)

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html
    stock_data['return'] = np.log(stock_data['price'] / stock_data['price'].shift(1))
    # .shift() does the following
    # 1 2 3 4 5 becomes
    #   1 2 3 4 5 (so in this case it becomes 2/1, 3/2, 4/3, 5/4 and so on)

    stock_data['move'] = stock_data['price'] - stock_data['price'].shift(1)

    # https://numpy.org/doc/stable/reference/generated/numpy.where.html
    # If we calculate average the 0 values do not count since there has been no move in price
    stock_data['up'] = np.where(stock_data['move'] > 0, stock_data['move'], 0)
    stock_data['down'] = np.where(stock_data['move'] < 0, stock_data['move'], 0)

    # Calculate RSI
    stock_data['average_gain'] = stock_data['up'].rolling(14).mean()
    stock_data['average_loss'] = stock_data['down'].abs().rolling(14).mean()
    RS = stock_data['average_gain'] / stock_data['average_loss']
    stock_data['RSI'] = 100.0 - (100.0 / (1.0 + RS))

    stock_data = stock_data.dropna()

    print(stock_data)

    plt.plot(stock_data['RSI'])
    plt.title('IBM - Relative Strength Indicator')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.show()