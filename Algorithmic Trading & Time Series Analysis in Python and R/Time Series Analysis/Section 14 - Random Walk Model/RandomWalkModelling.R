# Use random walk for modelling stock data

# install packages
install.packages("quantmod")

# import the specific library
require("quantmod")

# download the data from Yahoo Finance
getSymbols("^GSPC", source = "yahoo")

# Plot the historical data
plot(Ad(GSPC))

# Plot the Correlogram adjusted prices of GSPC
# with differencing to transform it to a stationary process

# we can see that random walk doesn't work well because
# there's still high amounts of correlation
acf(diff(Ad(GSPC)), na.action = na.omit)