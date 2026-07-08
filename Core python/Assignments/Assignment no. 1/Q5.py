#Compound Interest
##Take inputs for P,R,T
P = int(input('Enter the principal ammount:'))
R = int(input('Enter the rate of interest:'))
T = int(input('Enter the time in years:'))

##Calculate compound interest
CI = P * (1 + R/100) ** T - P

##Display the result
print('The compound interest is : ',CI)