##Take inputs for P,R,T
P = int(input('Enter the principal ammount:'))
R = int(input('Enter the rate of interest:'))
T = int(input('Enter the time in years:'))

##Calculate simple interest
SI = (P * R * T) / 100

##Display the result
print('The simple interest is : ',SI)