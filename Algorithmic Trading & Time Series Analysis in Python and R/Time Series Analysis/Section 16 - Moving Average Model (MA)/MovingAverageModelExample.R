# MA Model Example

# Set Seed
set.seed(1)

# Random Values
w <- rnorm(1000, mean = 0, sd = 1)

# Initialize Time Series
x <- rep(0, 1000)

# First order moving average model MA(2)
for(t in 3:1000) x[t] <- w[t] + 0.4*w[t-1] + 0.9*w[t-2]

plot(x, type='l')
# We can tell this is a MA(2) since 
# the first two true terms are outside the 95% mark by a lot
acf(x)

# Auto regressive set to 0
# Integrated Parts set to 0
# Moving Average set to 1 (since this is what we want)
ma <- arima(x, order = c(0, 0, 2))
ma
# Returns that it is a ma of second order
# and beta value is approx 0.4 and 0.9 respectively as set above
# Coefficients:
#         ma1     ma2     intercept
#       0.4065  0.9156    -0.0423
# s.e.  0.0122  0.0144     0.0763
# s.e. = standard error
# sigma^2 estimated as 1.069:  log likelihood = -1452.21,  aic = 2910.42