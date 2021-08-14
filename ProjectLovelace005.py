#Project Lovelace, Problem 5
#Compound interest

#Calculate the compound interest

import time

def compound_interest(amount, rate, years):
    """This function returns the true value if given compound interest"""
    return amount*(1+rate)**years

start = time.time()
print(compound_interest(1000,0.1,25))
print(time.time() - start)
#0.0 secs