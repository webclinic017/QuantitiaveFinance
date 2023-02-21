# First Comprehensive Trading Strategy based on Momentum

# https://www.investopedia.com/articles/technical/081501.asp

# Momentum= V − Vx
# where:
#     V = Latest price
#     Vx = Closing price
#     x = Number of days ago

import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy as np
from scipy.stats import linregress
import pandas as pd

def calculate_momentum(data):
    log_data = np.log(data)
    x_data = np.arange(len(log_data))
    beta, _, rvalue, _, _ = linregress(x_data, log_data) # becomes exponential regression since we are logging data
    # we have to annualize the slope
    # there are 252 trading days in a year
    momentum = (1+beta)**252 * (rvalue**2) # rvalue helps with checking accuracy
    return momentum

def download_stocks(stocks, start, end):
    data = {}

    for stock in stocks:
        ticker = yf.download(stock, start, end)
        data[stock] = ticker['Adj Close']

    return pd.DataFrame(data)

if __name__ == '__main__':

    start_date = datetime.datetime(2015, 1, 1)
    end_date = datetime.datetime(2018, 1, 1)

    stocks = ['IBM', 'TSLA', 'MSFT', 'AAPL', 'XOM', 'CVX', 'INTC']

    stocks_data = download_stocks(stocks, start_date, end_date)
    print(stocks_data)

    momentums = pd.DataFrame(columns=stocks)

    for stock in stocks:
        momentums[stock] = stocks_data[stock].rolling(90).apply(calculate_momentum, raw=False)

    print(momentums)

    # Don't worry to much about plotting it's just for show
    plt.figure(figsize=(12, 9))
    plt.xlabel('Days')
    plt.ylabel('Stock Price')

    bests = momentums.max().sort_values(ascending=False).index[:5]
    print(momentums.max().sort_values(ascending=False)[:5])
    for best in bests:
        end = momentums[best].index.get_loc(momentums[best].idxmax())
        returns = np.log(stocks_data[best].iloc[end - 90: end])
        x = np.arange(len(returns))
        slope, intercept, r_value, p_value, std_err = linregress(x, returns)
        plt.plot(np.arange(len(stocks_data[best][end - 90:end + 90])), stocks_data[best][end - 90:end + 90])
        plt.plot(x, np.e ** (intercept + slope * x))

    plt.show()




