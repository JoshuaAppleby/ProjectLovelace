#Project Lovelace, Problem 14
#Habitable exoplanets

#Using Luminosity and Distance from a star to decide if the planet is habitable

import time
import math

def habitable_exoplanet(L, r):
    """This function returns the habitability of a planet given the luminocity and distance of the main star"""
    inner = math.sqrt(L/1.1)
    outer = math.sqrt(L/0.54)
    if outer > r and inner < r:
        return "Just right"
    if outer < r:
        return "Too cold"
    return "Too hot"

start = time.time()
print(habitable_exoplanet(1.5,2.5))
print(time.time() - start)
#0.0 secs