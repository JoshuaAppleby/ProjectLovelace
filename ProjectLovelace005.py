#Project Lovelace, Problem 5
#Compound interest

"""Calculate the compound interest
"""

import time

def compound_interest(amount, rate, years):
    return amount*(1+rate)**years

start = time.time()
print(compound_interest(1000,0.1,25))
print(time.time() - start)
#0.00021910667419433594