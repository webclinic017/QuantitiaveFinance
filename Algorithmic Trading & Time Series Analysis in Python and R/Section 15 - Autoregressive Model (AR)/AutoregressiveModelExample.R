# Autoregressive Model (AR) Example

# generate the values for w(t) white noise
# default values mean = 0, sd = 1
w <- rnorm(1000)

# generate the x(t) values for the time series
# x(t=0) = x(t=1) = 0
x <- rep(0, 1000)

# we simulate AR(2) "second order"
# first 2 values will not have 2 values behind it so we start at index 3s
# this is the generator process
for (t in 3:1000) x[t] = 0.6*x[t-1]-0.4*x[t-2]+w[t]

plot(x, type='l')

# not a stationary process
acf(x)

# https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/ar
# Built in AR function
x.ar = ar(x, method="mle")

x.ar$order # returns 2 for second order process
x.ar$ar # returns 0.6260489 -0.3865779 for 0.6 -0.4 alpha parameters we set above
