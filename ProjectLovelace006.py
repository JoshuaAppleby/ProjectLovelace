#Project Lovelace, Problem 6
#Wind chill

#If you go outside when it's cold (below 5°C) and windy, you probably noticed that it feels colder than what the temperature says it is. 
#This is because cold air is passing around your body, lowering your body's temperature and making you feel colder.
#T_wc = 13.12 + 0.6215(T_a) - 11.37(v)**0.16 + 0.3965(T_a)(v)**0.16

import time

def wind_chill(T_a, v):
    """Returns the felt temperature when given the actual temperature and the windspeed"""
    return 13.12 + 0.6215*(T_a) - 11.37*(v)**0.16 + 0.3965*(T_a)*(v)**0.16

start = time.time()
print(wind_chill(-25,30))
print(time.time() - start)
#0.0 secs