def simpleInterest(p, r, t):
    return (p * r * t) / 100

p = int(input('Enter the principal value: '))
r = int(input('Enter the rate: '))
t = int(input('Enter the time: '))

si = simpleInterest(p, r, t)
print('The simple interest is:', si)