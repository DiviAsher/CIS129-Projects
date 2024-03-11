# Module 5 Lab - Bottle return program
# Divinity Asher
# 02/29/2024
# This program receives data about the amount of bottles returned in a week and calculates the total payout after the week

from decimal import Decimal

# Initialize variables for enabling the loop statement, tracked bottles, and tracked payout 
keepGoing = 'y'
counter = 1
todayBottles = 0
totalBottles = 0
totalPayout = 0

# Process local functions
def getBottles():
    todayBottles = int(input('Enter number of bottles returned for day # ' + str(counter) + ':'))   # User input for a day's worth of bottles
    totalBottles += todayBottles   # Accumulation of bottles from the week.
    totalPayout += todayBottles * .10   # Accumulated payout from the week's worth of bottles
    counter += 1   # Counter to track the day of the week for data input
    continue

def calcPayout():
    print('The total number of bottles collected is ', totalBottles)   # print 
    print('The total paid out is $', f'{totalPayout:.2f}')

# Termiate functions
if counter == 1:
    getBottles()
elif counter == :
    calcPayout()
    keepGoing = input("Do you want to enter another week's worth of data? \n(Enter y or n):")
