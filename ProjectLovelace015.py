#Project Lovelace, Problem 15
#Chaos

#Population Chaos: x(n+1) = rx(n)*(1-x(n))
# 0 < r < 4

import time

def logistic_map(r):
    """Returns the first 51 values of the chaos"""
    x = [0.5]
    for i in range(0,50):
        x.append(x[i]*r*(1-x[i]))
    return x

start = time.time()
print(logistic_map(2.81))
print(time.time() - start)
#0.0 secs