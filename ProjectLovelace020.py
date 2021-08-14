#Project Lovelace, Problem 20
#Molecular mass calculator

import time
import numpy as np
import pandas as pd
import re

def MolecularMassCalc(chemical_formula):
    """
    
    """
    data = pd.read_csv("https://projectlovelace.net/static_prod/resources/periodic_table.csv", header=None)
    split = re.split('(?=[A-Z])', chemical_formula)[1:]
    mass = 0
    for i in split:
        chemical_section = re.split('(\d+)', i)
        if len(chemical_section) == 1:
            row = data.index[data.iloc[:,0].str.contains(chemical_section[0])]
            index = int(row[0])
            element = data.iloc[index,1]
            mass += element
        else:
            row = data.index[data.iloc[:,0].str.contains(chemical_section[0])]
            index = int(row[0])
            element = data.iloc[index,1]
            mass += (element*int(chemical_section[1]))
    return mass

start = time.time()
print(MolecularMassCalc("C6H8K8O2"))
print(time.time() - start)
#0.5727121829986572 secs