# Modelling Assets with AR

# Install and initialize library
install.packages("quantmod")
require("quantmod")

# Download IBM stock data
# default: src = "yahoo"
getSymbols("IBM")

plot(Ad(IBM))

# let's calculate the log daily return
# x(t)    diff = x(t+1) - x(t)
#         log(diff) = log x(t+1) - log x(t) = log(x(t+1) / x(t)) 
returns = diff(log(Ad(IBM)))
plot(returns)
# stock prices are usually non stationary processes
# transforming with log diff turns it into a stationary process

acf(returns, na.action = na.omit)

model = ar(returns, na.action=na.omit)
model
# Coefficients:
#  1        2        3        4        5        6        7        8  
# -0.0294   0.0108   0.0029  -0.0366  -0.0028  -0.0413   0.0390  -0.0561  
# 9       10  
# 0.0404   0.0281  
# Order selected 10  sigma^2 estimated as  0.0002238

model$order # order 10 model
model$ar # returns alpha params like above
model$asy.var # returns variance

# residual series = actual values - predicted values by the model
# calculate error of the model
model$resid # The smaller the values the better
acf(model$resid, na.action=na.omit)
# Very low correlation which is really good

