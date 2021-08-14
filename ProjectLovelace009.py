#Project Lovelace, Problem 9
#Temperature Variations

#Calculating the mean and standard deviation for data in a list.

import time
from math import sqrt

def mean(a):
    """This function returns the mean for a list of data"""
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total/len(a)

def standarddev(a):
    """This function returns the standard deviation for a list of data"""
    average = mean(a)
    numerator = 0
    for i in range(len(a)):
        numerator += (a[i] - average)**2
    stdev = sqrt(numerator/len(a))
    return stdev


temperatures = [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]
start = time.time()
print(mean(temperatures))
print(standarddev(temperatures))
print(time.time() - start)
#0.0 secs