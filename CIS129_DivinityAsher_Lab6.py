# CIS129_DivinityAsher_Lab6
# Divinity Asher
# 03/04/2024

totalHotDogs = 0   # Accumulator of hot dog total

totalHotDogs = getTotalHotDogs();   # Calls the function to receive input necessary to calculate the minimimum number of hot dogs needed and assigns it to the accumulator variable.
showResults();   # Calls the function to show number of hot dogs and buns left over

def getTotalHotDogs():
    """Prompts user to input the amount of attendees attending as well as the amount of hot dogs allowed per attendee"""
    attendees = int(input('What is the maximum number of attendees for the cookout? '))   # Asks the user for the number of attendees for the cookout
    hotDogs = int(input('How many designated hot dogs per attendee? '))   # Asks the user for the amount of hot dogs per attendee
    Total = attendees * hotDogs
    return Total

def showResults():
    """Calculates the minimum amount of hot dogs and buns needed, the hot dogs and buns remaining, and prints said results"""
    global totalHotDogs
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS
    minDogs = (totalHotDogs / DOGS) + (0 ** (0 ** dogsLeft))
    minBuns = (totalHotDogs / BUNS) + (0 ** (0 ** bunsLeft))
    print('Minimum packages of hot dogs needed ', minDogs)
    print('Minimum packages of hot dog buns needed ', minBuns)
    print('Hot dogs remaining ', dogsLeft)
    print('Hot dogs bun remaining ', bunsLeft)
