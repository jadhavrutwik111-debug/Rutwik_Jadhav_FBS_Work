#calculte ticket amount for five people
p1 = int(input('Enter the age of person 1: '))
p2 = int(input('Enter the age of person 2: '))
p3 = int(input('Enter the age of person 3: '))
p4 = int(input('Enter the age of person 4: '))
p5 = int(input('Enter the age of person 5: '))

ticket = float(input('Enter the ticket amount: '))

#person 1
if(p1 < 12):
    amount1 = ticket - (ticket * 0.30)
elif(p1 > 59):
    amount1 = ticket - (ticket * 0.5)
else:
    amount1 = ticket

#person 2
if(p2 < 12):
    amount2 = ticket - (ticket * 0.30)
elif(p2 > 59):
    amount2 = ticket - (ticket * 0.5)
else:
    amount2 = ticket

#person 3
if(p3 < 12):
    amount3 = ticket - (ticket * 0.30)
elif(p3 > 59):
    amount3 = ticket - (ticket * 0.5)
else:
    amount3 = ticket

#person 4
if(p4 < 12):
    amount4 = ticket - (ticket * 0.30)
elif(p1 > 59):
    amount4 = ticket - (ticket * 0.5)
else:
    amount4 = ticket

#person 5
if(p5 < 12):
    amount5 = ticket - (ticket * 0.30)
elif(p5 > 59):
    amount5 = ticket - (ticket * 0.5)
else:
    amount5 = ticket

amount = amount1 + amount2 + amount3 + amount4 + amount5
print('Total ticket amount is:', amount)
