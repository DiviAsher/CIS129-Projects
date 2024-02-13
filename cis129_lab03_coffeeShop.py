#cis129_lab03_coffeeShop.py
#Variables for coffee, muffin, and tax prices
coffeeValue = 5
muffinValue = 4
tax = .06

#Inputs for coffee and muffin totals
coffeeTotal = int(input('How many coffees would you like to order? '))
muffinTotal = int(input('How many muffins would you like to order? '))

#Gross total for the total transaction
grossTotal = float((coffeeValue * coffeeTotal) + (muffinValue * muffinTotal))

#Amount of items purchased
print('***************************************');
print('Divine Caffeine Coffee Shop');
print('Number of coffees bought?');
print(coffeeTotal);
print('Number of muffins bought?');
print(muffinTotal);
print('***************************************');
#Total price calculations with tax reductions
print('***************************************');
print('Divine Caffeine Coffee Shop Receipt');
print(coffeeTotal, ' Coffee(s) at $5 each: $', float(coffeeValue * coffeeTotal));
print(muffinTotal, ' Muffin(s) at $4 each: $', float(muffinValue * muffinTotal));
print('6% tax: $', float(tax * grossTotal));
print('---------');
print('Total: $', float(grossTotal +  (grossTotal * tax)));
print('***************************************');
