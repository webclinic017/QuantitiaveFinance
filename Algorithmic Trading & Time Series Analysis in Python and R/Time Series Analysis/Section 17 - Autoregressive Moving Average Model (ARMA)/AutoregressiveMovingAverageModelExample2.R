# ARMA Model Example 2
# Find optimal order

# we can construct an ARMA(p, q) simulation with the AR and MA components
#              white noise            alpha params          beta params
x <- arima.sim(n=2000, model=list(ar=c(0.4, -0.2, 0.6), ma=c(0.6,-0.4)))

plot(x)

# Calculate the optimal q and p values with AIC
solution.aic <- Inf
solution.order <- 

# brute force method
for(i in 1:4) for(j in 1:4) {
  #                                        maximum iterationss
  actual.aic <- AIC(arima(x,order=c(i,0,j),optim.control=list(maxit = 1000)))
  
  if(actual.aic < solution.aic){
    solution.aic <- actual.aic
    solution.order <- c(i,0,j)
    solution.arma <- arima(x,order=solution.order,optim.control=list(maxit=1000))
  }
}

solution.aic      # 5650.838
solution.order    # 3 0 2

solution.arma
# Coefficients:
#       ar1      ar2     ar3     ma1      ma2       intercept
#       0.3913  -0.1740  0.5988  0.6246  -0.3754    -0.1636       # Finds approx alpha and beta
# s.e.  0.0272   0.0196  0.0182  0.0331   0.0331     0.1493
# sigma^2 estimated as 0.9759:  log likelihood = -2818.42,  aic = 5650.84

# no serial correlation in the residual y(t) series (differnece between time and actual series)
acf(resid(solution.arma))

# Let's apply the Ljung-Box Test
# If the -value > 0.05 it means that the residuals are independent
# at the 95% level so ARMS model is a good model
Box.test(resid(solution.arma), lag=20, type='Ljung-Box')
# data:  resid(solution.arma)
# X-squared = 6.3687, df = 20, p-value = 0.9983
