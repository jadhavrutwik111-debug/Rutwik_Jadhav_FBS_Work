num = int(input('Enter the number of passengers: '))
ticket = int(input('Enter the ticket cost: '))
total = 0
for i in range(1, num + 1):
    age = int(input(f'Enter the age of passenger {i}: '))

    if(age < 12):
        total += ticket * 0.7
    elif(age > 59):
        total += ticket * 0.5
    else:
        total += ticket

print(f'The total ticket amount is {total}')