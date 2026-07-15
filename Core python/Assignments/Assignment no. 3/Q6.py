#profit or loss
#take input for cost price and selling price
cp = float(input('Enter the cost price: '))
sp = float(input('Enter the selling price: '))

if(sp > cp):
    profit = sp - cp
    print('profit:',profit)
elif(sp < cp):
    loss = cp - sp
    print('loss:',loss)
else:
    print('No profit, no loss.')