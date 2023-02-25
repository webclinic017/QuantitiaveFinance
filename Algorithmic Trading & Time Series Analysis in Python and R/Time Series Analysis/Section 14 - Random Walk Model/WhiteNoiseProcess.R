# White noise example

# Computers can't generate true random so we define a seed so each time we re-run 
# it will generate the same sudo-random numbers
set.seed(1)

# Generate 1000 random values with set mean and standard deviation
x <- rnorm(1000, mean = 0, sd = 1)
plot(x)

# auto-correlation function 
acf(x) # Items should be completely independent of each other