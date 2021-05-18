#Project Lovelace, Problem 3
#Plump moose

"""Bergmann's rule says that animals living in colder climates tend to be larger in size. 
    Swedish scientists measured the body mass of different moose populations in Sweden and found that the further north you go, 
    the bigger the moose get! Taking their data we can fit a line through it to predict the body mass of a moose at some latitude using the equation
    mass = a*latitude + b
    where a = 2.757, b = 16.793
"""

import time

def moose_body_mass(latitude):
    a = 2.757
    b = 16.793
    return a*latitude + b

start = time.time()
print(moose_body_mass(60.5))
print(time.time() - start)
#0.00012087821960449219 secs