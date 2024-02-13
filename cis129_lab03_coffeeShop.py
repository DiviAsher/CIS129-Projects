#cis129_lab03_coffeeShop.py
#Variables for coffees, muffins, teas, bananas, and tax prices
coffeeValue = 5
muffinValue = 4
teaValue = 3
bananaValue = .5
tax = .06

#Inputs for coffee and muffin totals
coffeeTotal = int(input('How many coffees would you like to order? '))
muffinTotal = int(input('How many muffins would you like to order? '))
teaTotal = int(input('How many teas would you like to order? '))
bananaTotal = int(input('How many bananas would you like to order? '))

#Gross total for the total transaction
grossTotal = float((coffeeValue * coffeeTotal) + (muffinValue * muffinTotal) + (teaValue * teaTotal) + (bananaValue * bananaTotal))

#Amount of items purchased
print('***************************************');
print('Divine Caffeine Coffee Shop');
print('Number of coffees bought?');
print(coffeeTotal);
print('Number of muffins bought?');
print(muffinTotal);
print('Number of teas bought?');
print(teaTotal);
print('Number of bananas bought?');
print(bananaTotal);
print('***************************************');
#Calculations of item totals as well as net total calculation
print('***************************************');
print('Divine Caffeine Coffee Shop Receipt');
print(coffeeTotal, ' Coffee(s) at $5 each: $', float(coffeeValue * coffeeTotal));
print(muffinTotal, ' Muffin(s) at $4 each: $', float(muffinValue * muffinTotal));
print(teaTotal, ' Tea(s) at $3 each: $', float(teaValue * teaTotal));
print(bananaTotal, ' Banana(s) at $.50 each: $', float(bananaValue * bananaTotal));
print('6% tax: $', float(tax * grossTotal));
print('---------');
print('Total: $', float(grossTotal +  (grossTotal * tax)));
print('***************************************');
print('Thank you again for blessing us with YOUR Divine presence!')
