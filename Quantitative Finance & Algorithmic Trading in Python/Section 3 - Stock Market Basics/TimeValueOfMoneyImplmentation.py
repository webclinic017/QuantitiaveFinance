from math import exp

def future_discrete_value(x, r, n):
    return x*((1+r)**n)

def present_discrete_value(x, r, n):
    return x/((1+r)**n) # or x*((1+r)**-n)

def future_continuous_value(x, r, t):
    return x*(exp(r*t))

def present_continuous_value(x, r, t):
    return x*(exp(-r*t))

if __name__ == '__main__':

    # Value of investment in $
    x = 100
    # Interest rate of 5%
    r = 0.05
    # Duration of 5 years
    n = 5

    print('Future value (discrete model) of x: %s' % future_discrete_value(x, r, n))
    print('Present value (discrete model) of x: %s' % present_discrete_value(x, r, n))
    print('Future value (continuous model) of x: %s' % future_continuous_value(x, r, n))
    print('Present value (continuous model) of x: %s' % present_continuous_value(x, r, n))
    
    # Future value (discrete model) of x: 127.62815625000003
    # Present value (discrete model) of x: 78.35261664684589
    # Future value (continuous model) of x: 128.40254166877415
    # Present value (continuous model) of x: 77.8800783071405



