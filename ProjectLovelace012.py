#Project Lovelace, Problem 12
#Definite Integrals

#Works out the area under rectangles (integration) if given list of rectangle heights and a width.

import time

def area(rectlist, width):
    """This function returns the total area under the rectangles."""
    return width*sum(rectlist)

start = time.time()
print(area([-1, 2, -3, 4, -5],2))
print(time.time() - start)
#0.0009992122650146484 secs