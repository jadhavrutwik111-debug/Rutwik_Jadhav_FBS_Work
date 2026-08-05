def calculatePower(m, n):
    if(n > 0):
        return m * calculatePower(m, n - 1)
    else:
        return 1

m = int(input('Enter the number: '))
n = int(input('Enter the power: '))
pow = calculatePower(m, n)
print(f'The {m} to the power {n} is {pow}.')