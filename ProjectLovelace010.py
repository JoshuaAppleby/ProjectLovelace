#Project Lovelace, Problem 10
#Blood Types

#Given a patient's blood type and a list of available blood types figure out if the patient will survive.

import time

blood = {
    "O-":"AB-,AB+,O-,O+,B-,B+,A-,A+",
    "O+":"AB+,O+,B+,A+",
    "A-":"AB-,AB+,A-,A+",
    "A+":"AB+,A+",
    "B-":"AB-,AB+,B-,B+",
    "B+":"AB+,B+",
    "AB-":"AB-",
    "AB+":"AB-,AB+"
}

def isitokay(bloodtype,bloodavailable):
    """This function returns True or False dependant on if the blood needed is 
        available from the blood available after checking in the dictionary"""
    bloodlist = list(blood[bloodtype].split(","))
    for i in bloodavailable:
        if i in bloodlist:
            return True
    return False

Blood_needed = "B+"
Blood_available = ["A-", "B+", "AB+", "O+", "B+", "B-"]
start = time.time()
print(isitokay(Blood_needed,Blood_available))
print(time.time() - start)
#0.0 secs