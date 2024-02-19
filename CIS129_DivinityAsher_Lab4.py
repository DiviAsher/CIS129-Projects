# Module 4 Lab-4
# Divinity Asher
# 02/18/2024
# This program calculates and prints the bonuses received based on the store's sales amount

# Variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
salePrompt = "What is your shop's monthly sale amount?: $" # prompt for shop's monthly sale amount
incPrompt = "What is your shop's sale increase percentage?: "

# User inputs for monthly sales and increase rates
monthlySales = float(input(salePrompt))

# This code determines the store bonus based on monthly sales
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0

# This code calculates the sale increase percentage
salesIncrease = float(input(incPrompt))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus
if salesIncrease >= .05:
  empAmount = 75
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
  empAmount = 40
else:
  empAmount = 0

# This code prints the determined bonus amount and acknowledges whether the bonus is at its maximum.
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible!')
