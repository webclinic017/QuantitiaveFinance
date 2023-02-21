# Backtrader Framework Moving Average Example
# https://backtrader.com/docu/

import backtrader as bt
from datetime import datetime
import yfinance as yf


class MovingAverageStrategy(bt.Strategy):

    params = (('period_fast', 30), ('period_slow', 200))

    def __init__(self):
        # get the data we have provided
        self.close_data = self.data.close
        # usually this is where we create the indicators
        self.fast_sma = bt.indicators.MovingAverageSimple(self.close_data, period=self.params.period_fast)
        self.slow_sma = bt.indicators.MovingAverageSimple(self.close_data, period=self.params.period_slow)

    # this function will be called automatically after a new data point (stock price) is available
    def next(self):

        # check if we have already opened a long position
        if not self.position:
            # we can open a long position if needed
            # [0] is current day [-1] is previous day
            if self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] < self.slow_sma[-1]:
                #print('BUY')
                self.buy()
        else:
            # check whether to close long position or not
            if self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] > self.slow_sma[-1]:
                #print('CLOSE')
                self.close()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    # add data to the core
    stock_data = bt.feeds.PandasData(dataname=yf.download('MSFT', '2010-01-01', '2020-01-01', auto_adjust=True))

    # we have to add the data to Cerebro
    cerebro.adddata(stock_data)
    cerebro.addstrategy(MovingAverageStrategy)

    cerebro.addobserver(bt.observers.Value)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0)
    cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.DrawDown)

    # set portfolio value
    cerebro.broker.set_cash(3000) # Change intial investment amount
    print('Initial Capital: $%.2f' % cerebro.broker.getvalue()) # default value is $10,000

    # commission fees - set 0.1%
    cerebro.broker.setcommission(0.01)

    # run the strategy
    results = cerebro.run()

    # evaluate results
    print('Sharpe ratio: %.2f' % results[0].analyzers.sharperatio.get_analysis()['sharperatio'])
    print('Return: %.2f%%' % results[0].analyzers.returns.get_analysis()['rnorm100'])
    print('Max drawdown: %.2f%%' % results[0].analyzers.drawdown.get_analysis()['max']['drawdown'])

    print('Final Capital: $%.2f' % cerebro.broker.getvalue())

# Without Commision
# Initial Capital: $3000.00
# Sharpe ratio: 0.85
# Return: 0.44%
# Max drawdown: 0.65%
# Final Capital: $3133.86

# With Commision
# Initial Capital: $3000.00
# Sharpe ratio: -0.73
# Return: -1.66%
# Max drawdown: 17.25%
# Final Capital: $2537.22