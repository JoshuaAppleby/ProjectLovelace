#Project Lovelace, Problem 13
#Rocket science

#Calculate the mass of the fuel required for a rocket to escape the planet.
#m(fuel) = m(rocket)*(exp(velocity/exhaust velocity)-1)

import time
import math

def rocketfuel(velocity):
    """This function returns the mass of fuel required for a rocket given the needed velocity"""
    v_e = 2550
    massrocket = 250000
    mass = massrocket*(math.exp(velocity/v_e) - 1)
    return mass

start = time.time()
print(rocketfuel(11186.0))
print(time.time() - start)
#0.0 secs