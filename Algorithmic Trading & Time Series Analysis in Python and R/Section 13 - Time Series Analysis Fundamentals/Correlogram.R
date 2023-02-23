# Correlogram Understanding

# 100 Random Gaussian White Noise Values
w = rnorm(100)
w

# Autocorrelation Function
acf(w)
# If we have have most correlations within 95% 
# confidence level we can say it has no autocorrelation with 95% confidence
# and that the underlying time series is stationary
# This makes sense here since it's just random values


####################################################################

# 100 sequential values (trend)
w = seq(1:100)
w

# Autocorrelation Function
acf(w)
# We know this is a non-stationary process since there is
# autocorrelation between the values (trend)

#####################################################################

# 10 repeating values of 1-5 (seasonality)
w = rep(1:5, 10)

# With lag 0, 5, 10, 15 we see a large correlation 
# since the values match up as seen below
# 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 
#           1 2 3 4 5 

w

# Autocorrelation Function
acf(w)
# We know this is a non-stationary process since there is
# autocorrelation between the values (seasonality)





