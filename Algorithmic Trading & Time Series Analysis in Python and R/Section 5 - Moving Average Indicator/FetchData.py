# Extract Financial Data from Yahoo Finance

import yfinance as yf
import pandas as pd

def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

if __name__ == '__main__':
    start = '2010-01-05'
    end = '2015-01-05'
    stock_data = download_data('IBM', start, end)
    print(stock_data)

#                Price
# Date
# 2010-01-05   79.357697
# 2010-01-06   78.842163
# 2010-01-07   78.569260
# 2010-01-08   79.357697
# 2010-01-11   78.526802
# ...                ...
# 2014-12-26  108.335449
# 2014-12-29  107.114265
# 2014-12-30  106.807251
# 2014-12-31  107.067520
# 2015-01-02  108.148613
