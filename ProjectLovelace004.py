#Project Lovelace, Problem 4
#NAND gate

"""Make NOT, AND and NAND gates
    Inputs must be 0 or 1
"""

import time

def NOT(A):
    if A == 0:
        return 1
    return 0

def AND(A,B):
    if A == 1 and A == B:
        return 1
    return 0

def NAND(A,B):
    if A == 1 and A == B:
        return 0
    return 1

start = time.time()
print(NAND(1,0))
print(time.time() - start)
#0.0005910396575927734