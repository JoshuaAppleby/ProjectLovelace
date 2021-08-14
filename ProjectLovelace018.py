#Project Lovelace, Problem 18
#Colorful resistors

#Using a list of colors as input compute the nominal resistance (i.e. as told by the colored bands, whithout any tolerance), as well as the minimum and maximum resistance value of the resistor, and return them in that order.

import time

digits = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

multiplier = {
    'pink': 0.001,
    'silver': 0.01,
    'gold': 0.1,
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 10 ** 3,
    'yellow': 10 ** 4,
    'green': 10 ** 5,
    'blue': 10 ** 6,
    'violet': 10 ** 7,
    'grey': 10 ** 8,
    'white': 10 ** 9
}

tolerance = {
    'none': 0.2,
    'silver': 0.1,
    'gold': 0.05,
    'brown': 0.01,
    'red': 0.02,
    'green': 0.005,
    'blue': 0.0025,
    'violet': 0.001,
    'grey': 0.0005
}

def resistance(band_colours):
    """Returns the resistance values in Ohms if given the colour bands"""
    n_bands = len(band_colours)
    coeff = []
    if n_bands == 3:
        coeff.append(digits[band_colours[0]])
        coeff.append(multiplier[band_colours[1]])
        coeff.append(tolerance[band_colours[2]])
    elif n_bands == 4:
        coeff.append(int(str(digits[band_colours[0]])+str(digits[band_colours[1]])))
        coeff.append(multiplier[band_colours[2]])
        coeff.append(tolerance[band_colours[3]])

    elif n_bands == 5:
        coeff.append(int(str(digits[band_colours[0]])+str(digits[band_colours[1]])+str(digits[band_colours[2]])))
        coeff.append(multiplier[band_colours[3]])
        coeff.append(tolerance[band_colours[4]])
    else:
        return "Incorrent number of colours"
    nominal_R = coeff[0]*coeff[1]
    minimum_R = nominal_R - nominal_R*coeff[2]
    maximum_R = nominal_R + nominal_R*coeff[2]
    return nominal_R, minimum_R, maximum_R

band_colours = ["red", "orange", "violet", "black", "brown"]

start = time.time()
print(resistance(band_colours))
print(time.time() - start)
#0.0 secs