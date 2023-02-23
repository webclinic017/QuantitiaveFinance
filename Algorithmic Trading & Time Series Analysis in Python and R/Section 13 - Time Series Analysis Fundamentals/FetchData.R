# if you have not a;ready installed it you have to do this
install.packages("quantmod")

# this is how we fetch financial data from the web
require("quantmod")
# we want to fetch AAPL related stock prices
getSymbols("AAPL", src="yahoo", start="2010-01-05", to="2020-01-05")
getSymbols("TSLA", src="yahoo", start="2010-01-05", to="2020-01-05")
# AAPL # prints out data
# High (Hi), Low (Lo), Closing Prices (Cl), Adjusted Closing Prices (Ad)
AAPL$AAPL.Adjusted
# Ad(AAPL) Same as above

# Plotting
plot(Ad(TSLA))
