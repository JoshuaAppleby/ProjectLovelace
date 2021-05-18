#Project Lovelace, Problem 2
#Speed of Light

"""How long will it take to travel a distance at the speed of light?
    C = 299792458 m/s
    Distance in meters
"""

import time

def light_time(distance):
    C = 299792458
    return distance/C

start = time.time()
print(light_time(376291900))
print(time.time() - start)
#0.0002067089080810547 secs