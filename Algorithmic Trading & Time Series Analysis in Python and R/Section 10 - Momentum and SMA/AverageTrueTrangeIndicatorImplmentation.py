# ATR Indicator Implementation

import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd


def download_data(stock, start, end):
    ticker = yf.download(stock, start, end)
    return pd.DataFrame(ticker)

def calculate_atr(data):
    high_low = data['High'] - data['Low']
    # .shift() helps us get previous value from previous day
    high_close = np.abs(data['High'] - data['Close'].shift())
    low_close = np.abs(data['Low'] - data['Close'].shift())

    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_ranges = np.max(ranges, axis=1)

    atr = true_ranges.rolling(14).sum() / 14
    # Equivalent as above
    # atr = true_ranges.rolling(14).mean()

    return atr

if __name__ == '__main__':

    start_date = datetime.datetime(2011, 4, 1)
    end_date = datetime.datetime(2013, 1, 1)

    stock_data = download_data('XOM', start_date, end_date)
    atr_values = calculate_atr(stock_data)

    # subplots to visualize data
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Stock Prices and ATR Indicator')
    ax1.plot(stock_data['Close'])
    ax2.plot(atr_values)
    plt.show()

    #print(stock_data)
    # plt.plot(stock_data['Close'])
    # plt.show()