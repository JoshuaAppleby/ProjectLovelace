#Project Lovelace, Problem 8
#Almost π

#The number =3.1415926535897... is the ratio of a circle's circumference to its diameter and shows basically everywhere in math and science. 
#It's like the most famous number in math. It's decimal expansion goes on forever but we can actually calculate it by summing up a bunch of fractions
#pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...

import time

def fractionlist(n):
    """This function returns a list of odd top heavy fractions"""
    frac = [1]
    for i in range(3,10000000,2):
        frac.append(i)
        if len(frac) == n:
            newfrac = [1/i for i in frac]
            return newfrac

def pi_approx(n):
    """This function calculates an approximation for pi using the fraction list"""
    listfraction = fractionlist(n)
    ans = 0
    for i in range(len(listfraction)):
        if i == 0:
            ans += 1
        elif i % 2 == 0:
            ans += listfraction[i]
        else:
            ans -= listfraction[i]
    return 4*ans

start = time.time()
print(pi_approx(1000))
print(time.time() - start)
#0.0 secs