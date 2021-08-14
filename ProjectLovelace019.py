#Project Lovelace, Problem 19
#Correlation does not imply causation

#Pearson correlation coefficient

import time
import numpy as np

def correlation_coefficient(x, y):
    """Returns the value of the Pearson correlation coefficient"""
    arrayx = np.array(x)
    arrayy = np.array(y)
    rarray = np.corrcoef(arrayx,arrayy)
    rset = set(rarray.flatten())
    cleanedlist = list(rset)
    for i in cleanedlist:
        if i == 1.0:
            continue
        else:
            return i
    else:
        return "ERROR"

x_in = [5427,5688,6198,6462,6635,7336,7248,7491,8161,8578,9000]
y_in = [18.079, 18.594, 19.753, 20.734, 20.831, 23.029, 23.597, 23.584, 22.525, 27.731, 29.449]

start = time.time()
print(correlation_coefficient(x_in, y_in))
print(time.time() - start)
#0.001994609832763672 secs