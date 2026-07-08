#calculate selling price 
#take inputs for cost price and discount
cp = int(input('Enter the cost price: '))
dis = int(input('Enter the discount: '))

#calculate selling price
sp = cp + cp * (dis/100)

#display result
print(f'Selling price of book is: {sp}.')