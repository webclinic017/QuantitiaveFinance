# Calculating Basics Stats
require("quantmod")

getSymbols("TSLA", src="yahoo", start="2010-01-05", to="2020-01-05")
getSymbols("IBM", src="yahoo", start="2010-01-05", to="2020-01-05")

# Transform data to get same dates
TSLA = TSLA[index(TSLA) > "2015-01-01"]
IBM = IBM[index(IBM) > "2015-01-01"]

plot(Ad(TSLA))
plot(Ad(IBM))

# Expected Value E(x) / Mean
mean(Ad(TSLA))
# $12.22434

# Standard Deviation
sd(Ad(TSLA)) # == sqrt(var(Ad(TSLA)))
# $7.64521

# Variance
var(Ad(TSLA))
# $58.44924

# Correlation betwwen TSLA and IBM
cor(Ad(IBM), Ad(TSLA))
# 0.1351879

# Covariance
cov(Ad(IBM), Ad(TSLA))
# 4.371544


