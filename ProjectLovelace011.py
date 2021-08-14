#Project Lovelace, Problem 11
#Babylonian Square Roots

#Iterative Babylonian method for square roots
#x(n+1) = 0.5(x(n) + S/x(n))

import time

def babylonian(S):
    """This function returns the square root of a number by the iterative babylonian method"""
    xn = S/2
    count = 0
    while count < 10:
        xnn = 0.5*(xn + S/xn)
        xn = xnn
        count += 1
    return xnn

start = time.time()
print(babylonian(420))
print(time.time() - start)
#0.0 secs