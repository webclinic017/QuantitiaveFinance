# Markowitz Model Implementation

import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# On average there are 252 trading days in a year
NUM_TRADING_DAYS = 252

# Generate random w (different portfolios)
NUM_PORTFOLIOS = 10000

# stocks we are going to handle and consider
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']

# historical data - define START and END dates
start_date = '2012-01-01'
end_date = '2017-01-01'

def download_data():
    # name of the stock (key) - stock values (2010-2017) as the values
    stock_data = {}

    for stock in stocks:
        # closing prices
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pd.DataFrame(stock_data)


def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()


def calculate_return(data):
    # NORMALIZATION - to measure all variables in comparable metric
    log_return = np.log(data/data.shift(1))
    # starting with second row since first is invalid because it doesn't have a previous value
    return log_return[1:]
    # shift function for s(t+1) / s(t)
    # 12345
    #  12345


def show_statistics(returns):
    # instead of daily metrics we are after annual metrics
    # The mean of annual returns
    print(returns.mean() * NUM_TRADING_DAYS)
    # The covariance of annual returns
    print(returns.cov() * NUM_TRADING_DAYS)


def show_mean_variance(returns, weights):
    # we are after the annual return
    portfolio_return = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
    # volatility = variance**2
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*NUM_TRADING_DAYS, weights)))

    print("Expected portfolio mean (return): ", portfolio_return)
    print("Expected portfolio volatility (standard deviation): ", portfolio_volatility)


def show_portfolios(returns, volatilities):
    plt.figure(figsize=(10, 6))
    plt.scatter(volatilities, returns, c=returns/volatilities, marker='o')
    plt.grid(True)
    plt.title('Efficiency Frontier Markowitz Modern Portfolio Theory')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()



def generate_portfolios(returns):

    portfolio_means = []
    portfolio_risks = []
    portfolio_weights = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))
        # Make sure sum of weights is 1
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_means.append(np.sum(returns.mean() * w) * NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov()*NUM_TRADING_DAYS, w))))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)


def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    return np.array([portfolio_return, portfolio_volatility, sharpe_ratio])


# Scipy Optimize module can find the minimum of a given function
# the maximum of a f(x) function is the minimum of -f(x)
def min_function_sharpe(weights, returns):
    return -statistics(weights, returns)[2]


# what are the constraints? the sum of the weights = 1
# sum of w = 1 --> w - 1 = 0
# f(x) = 0 this is the function to minimize
# https://docs.scipy.org/doc/scipy/reference/optimize.html
def optimize_portfolio(weights, returns):
    # the sum of weights is 1
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    # the weights can be 1 at most when 100% of the money is invested into a single stock
    bounds = tuple((0, 1) for _ in range(len(stocks)))
    return optimization.minimize(fun=min_function_sharpe, x0=weights[0], args=returns, method='SLSQP',
                                 bounds=bounds, constraints=constraints)


def print_optimal_portfolio(optimum, returns):
    print("Optimal portfolio: ", optimum['x'].round(3))
    print('Expected Return, Volatility, and Sharpe Ratio: ',
          statistics(optimum['x'].round(3), returns))


def show_optimal_portfolio(opt, rets, portfolio_rets, portfolio_vols):
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_vols, portfolio_rets, c=portfolio_rets / portfolio_vols, marker='o')
    plt.grid(True)
    plt.title('Efficiency Frontier Markowitz Modern Portfolio Theory with Optimization')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(opt['x'], rets)[1], statistics(opt['x'], rets)[0], 'g*', markersize=20.0)
    plt.show()


if __name__ == '__main__':

    dataset = download_data()
    log_daily_returns = calculate_return(dataset)
    show_data(dataset)
    # print(show_statistics(log_daily_returns))

    portfolio_weights, means, risks = generate_portfolios(log_daily_returns)
    show_portfolios(means, risks)

    optimum = optimize_portfolio(portfolio_weights, log_daily_returns)
    print_optimal_portfolio = print_optimal_portfolio(optimum, log_daily_returns)
    show_optimal_portfolio(optimum, log_daily_returns, means, risks)

    #              Optimal Weights of each stock from stocks list above
    # Optimal portfolio:  [0.14  0.    0.166 0.373 0.321 0.   ]
    # Expected Return, Volatility, and Sharpe Ratio:  [0.23456036 0.19523433 1.20142992]

