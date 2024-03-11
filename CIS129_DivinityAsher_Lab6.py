# CIS129_DivinityAsher_Lab6 - Hotdog Cookout Lab 
# Divinity Asher
# 03/04/2024

totalHotDogs = 0   # Accumulator of hot dog total

def getTotalHotDogs():
    """Prompts user to input the amount of attendees attending as well as the amount of hot dogs allowed per attendee"""
    attendees = int(input('What is the maximum number of attendees for the cookout?: '))   # Asks the user for the number of attendees for the cookout
    hotDogs = int(input('How many designated hot dogs per attendee?: '))   # Asks the user for the amount of hot dogs per attendee
    totalHotDogs = attendees * hotDogs   
    return totalHotDogs

def showResults():
    """Calculates the minimum amount of hot dogs and buns needed, the hot dogs and buns remaining, and prints said results"""
    global totalHotDogs   # Passes totalHotDogs on a global scale as an argument in this function
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS   # Calculates the amount of hot dogs left
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS   # Calculates the amount of hot dog buns left
    minDogs = (totalHotDogs / DOGS) + (0 ** (0 ** dogsLeft))   # Calculates the minimum number of hot dogs needed for the cookout
    minBuns = (totalHotDogs / BUNS) + (0 ** (0 ** bunsLeft))   # Calculates the minimum number of hot dog buns needed for the cookout
    # Prints the results of the calculations for the user
    print('Minimum packages of hot dogs needed: ', minDogs)
    print('Minimum packages of hot dog buns needed: ', minBuns)
    print('Hot dogs remaining: ', dogsLeft)
    print('Hot dogs bun remaining: ', bunsLeft)

totalHotDogs = getTotalHotDogs();   # Calls the function to receive input necessary to calculate the minimimum number of hot dogs needed and assigns it to the accumulator variable.
showResults();   # Calls the function to show number of hot dogs and buns left over
