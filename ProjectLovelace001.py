#Project Lovelace, Problem 1
#Scientific temperatures

"""Conversion between Celcius and Fahrenheit.
    C = (5/9)*(F-32)
"""

import time

def fahrenheit_to_celsius(F):
    C = (5/9)*(F-32)
    return C

def celsius_to_fahrenheit(C):
    F = ((9*C)/5)+32
    return F

start = time.time()
print(fahrenheit_to_celsius(100))
print(celsius_to_fahrenheit(37.77777777777778))
print(time.time() - start)
#0.0009975433349609375 secs