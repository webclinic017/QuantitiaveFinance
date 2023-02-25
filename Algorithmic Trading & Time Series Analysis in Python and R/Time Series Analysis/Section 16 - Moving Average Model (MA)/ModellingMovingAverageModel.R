# Modelling with MA Model

install.packages("quantmod")
require("quantmod")

getSymbols('AAPL', src = 'yahoo')

plot(Ad(AAPL))

# log daily returns
returns = diff(log(Ad(AAPL)))
plot(returns)

acf(returns, na.action = na.omit)

ma = arima(returns, order = c(0,0,3))
ma
# Since Beta values are very small it is mainly the white
# noise that is dominant

# Check residuals except first NA one
acf(ma$res[-1])
# This model is not able to explain the auto correlation
# so it is not that good
