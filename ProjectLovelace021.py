#Project Lovelace, Problem 21
#El Niño intensities

import time
import pandas as pd

def enso_classification(year):
    data = pd.read_table("https://projectlovelace.net/static_prod/resources/mei.ext_index.txt")
    row = (data.loc[data["YEAR"] == year])
    figures = []
    for i in range(12):
        figures.append(row.iloc[:,1+i:2+i])
    final = []
    for i in figures:
        placeholder = float(str(i)[-7:])
        final.append(placeholder)
    maximum = max(final)
    minimum = abs(min(final))
    strength = 0
    if maximum > minimum and maximum >= 0.5:
        classification = "El Nino"
        strength = 1
        test = maximum
    elif maximum < minimum and minimum >= 0.5:
        classification = "La Nina"
        strength = 1
        test = minimum
    else:
        classification = "Neither"
        strength = "None"
    if strength == 0:
        return classification, strength
    elif strength == 1:
        if test >= 2:
            strength = "Very Strong"
        elif test >= 1.5:
            strength = "Strong"
        elif test >= 1.0:
            strength = "Moderate"
        else:
            strength = "Weak"
    return classification, strength

start = time.time()
print(enso_classification(2016))
print(time.time() - start)
#0.7073326110839844 secs