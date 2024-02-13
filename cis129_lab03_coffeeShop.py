#cis129_lab03_coffeeShop.py
#Variables for coffee, muffin, and tax prices
coffeeValue = 5
muffinValue = 4
tax = .6

#Inputs for coffee and muffin totals
coffeeTotal = int(input('How many coffees would you like to order? '))
muffinTotal = int(input('How many muffins would you like to order? '))

#Gross total for the total transaction
grossTotal = float((coffeeValue * coffeeTotal) + (muffinValue * muffinTotal))

#Final printed receipt information
print('***************************************',\
     'Divine Caffeine Coffee Shop',\
     'Number of coffees bought?',\
     coffeeTotal,\
     'Number of muffins bought?',\
     muffinTotal,\
     '***************************************',\
     \
     '***************************************',\
     'Divine Caffeine Coffee Shop Receipt',\
     coffeeTotal, ' Coffee(s) at $5 each: $', float(coffeeValue * coffeeTotal),\
     muffinTotal, ' Muffin(s) at $4 each: $', float(muffinValue * muffinTotal),\
     '6% tax: $', float(tax * grossTotal),\
     '---------',\
     'Total: $', float(grossTotal +  (grossTotal * tax)),\
     '***************************************')
