#Project Lovelace, Problem 7
#Flight paths

#You can calculate the length of the curved path using the haversine formula.
#Path = 2R*arcsin(sqrt(sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)))

import time
from math import radians, sqrt, asin, sin, cos

def haversine_distance(lat1,lon1,lat2,lon2):
    """Returns the curved path length when given the longitude and latitudes of two points"""
    R = 6372.1
    coefficient1 = 2*R
    firstsin = (sin(radians((lat2-lat1)/2)))**2
    coscos = (cos(radians(lat1)))*(cos(radians(lat2)))
    secondsin = (sin(radians((lon2-lon1)/2)))**2
    return coefficient1*(asin((sqrt(firstsin + coscos*secondsin))))

start = time.time()
print(haversine_distance(46.283,86.667,-48.877,-123.393))
print(time.time() - start)
#0.0 secs