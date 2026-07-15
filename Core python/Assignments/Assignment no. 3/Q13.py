#electricity bill calculator
units = int(input('Enter the number of units:'))

if(units <= 50):
    bill = units * 0.5
elif(units <= 150):
    bill = 50 * 0.5 + (units - 50) * 0.75
elif(units <= 250):
    bill = 50 * 0.5 + 100 * 0.75 + (units - 150) * 1.2
else:
    bill = 50 * 0.5 + 100 * 0.75 + 100 * 1.2 + (units - 250) * 1.5

surcharge = bill * 0.2
bill = bill + surcharge

print(bill)
