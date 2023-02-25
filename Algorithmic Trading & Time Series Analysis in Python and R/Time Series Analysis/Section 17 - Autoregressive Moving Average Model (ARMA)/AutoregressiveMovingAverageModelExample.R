# ARMA Model Example
# p value test

install.packages('lmtest')
require('lmtest')

# We can construct a ARMA(p, q) simulation with the AR and MA components
x = arima.sim(n = 1000, model=list(ar=0.4, ma=-0.2)) # ar = alpha, ma = beta (changing these values can lead to better p value results)

# auto-reggrssive 1 and moving average 1
model = arima(x, order=c(1,0,1))

model
# Coefficients:
#        ar1      ma1    intercept
#      0.4033  -0.2130    -0.0105
#s.e.  0.1248   0.1326     0.0434
#sigma^2 estimated as 1.082:  log likelihood = -1458.46,  aic = 2924.92

coeftest(model)
#z test of coefficients:
  
#            Estimate Std. Error z value Pr(>|z|)   
# ar1        0.403326   0.124811  3.2315 0.001231 ** For alpha p value is < 0.05 so it is significant
# ma1       -0.213032   0.132594 -1.6067 0.108131    For beta p value is > 0.05 so it is not significant
# intercept -0.010535   0.043371 -0.2429 0.808075   
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1