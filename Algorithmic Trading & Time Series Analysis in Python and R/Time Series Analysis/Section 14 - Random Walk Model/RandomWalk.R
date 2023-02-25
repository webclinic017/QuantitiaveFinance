# Random Walk Example

# we are generating white noise terms
w <- rnorm(2000, mean = 0, sd = 1)


# define the x time series (2000 0s to start)
x <- rep(0, 2000)

# random walk x(t) = x(t-1) + w(t)
# indexes start with 1 in R but we want first value to be 0 so we start with index 2
for (t in 2:2000) x[t] <- x[t-1] + w[t]

plot(x, type='l')

# A lot of auto/serial correlation will occur since random walk is a non stationary process
acf(x)

# we can use differencing operator to change non stationary to stationary process
# First value doesn't have any previous so we can omit it
# With diff() this becomes a stationary process and there is minimal correlation 
acf(diff(x), na.action = na.omit)