#Project Lovelace, Problem 16
#DNA transcription

#Conversion of DNA to RNA requires two steps, reversal and replacement of T to U

import time

def rna(dna):
    """This function returns the RNA code for inputted DNA code"""
    reverseddna = dna[::-1]
    rna = reverseddna.replace("T","U")
    return rna

start = time.time()
print(rna("CCTAGGACCAGGTT"))
print(time.time() - start)
#0.0 secs