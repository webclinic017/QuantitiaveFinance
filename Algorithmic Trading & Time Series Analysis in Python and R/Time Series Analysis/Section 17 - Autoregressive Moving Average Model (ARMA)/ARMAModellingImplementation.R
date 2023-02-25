# ARMA Modelling Implementation

install.packages('quantmod')
require('quantmod')

# Download S&P500 prices from yahoo Finance
getSymbols('^GSPC', src='yahoo')

# log daily returns
returns <- diff(log(Ad(GSPC)))

# calculate the optimal p and q values with AIC
solution.aic <- Inf
solution.order <- c(0,0,0)

# Brute force
for(i in 1:4) for(j in 1:4) {
  actual.aic <- AIC(arima(returns,order=c(i,0,j),optim.control=list(maxit = 1000)))
  
  # The lower the AIC the better the model
  if(actual.aic < solution.aic){
    solution.aic <- actual.aic
    solution.order <- c(i,0,j)
    solution.arma <- arima(returns,order=solution.order,optim.control=list(maxit=1000))
  }
}

solution.aic    # -23828.89
solution.order  # 3 0 2
solution.arma
# Coefficients:
#       ar1      ar2     ar3     ma1      ma2     intercept
#      0.3913  -0.1740  0.5988  0.6246  -0.3754    -0.1636
#s.e.  0.0272   0.0196  0.0182  0.0331   0.0331     0.1493

# autocorrelation plot
acf(resid(solution.arma), na.action=na.omit)

# Ljung-Box test for the y(t) resiudal series
Box.test(resid(solution.arma), lag=20, type='Ljung-Box')
# data:  resid(solution.arma)
# X-squared = 58.118, df = 20, p-value = 1.387e-05 ** p value is < 0.05
# So this model has serial correlation
