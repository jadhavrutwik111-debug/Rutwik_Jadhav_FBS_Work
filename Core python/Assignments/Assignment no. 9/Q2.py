def powerOfDigit(pow, a):
    return a ** pow

def checkArmstrong(num, pow):
    if(num > 0):
        d = num % 10
        return powerOfDigit(pow, d) + checkArmstrong(num // 10, pow)
    else:
        return 0

n = input('Enter the number: ')
a = len(n)
n = int(n)
res = checkArmstrong(n, a)

if(res == n):
    print(f'{n} is armstrong number.')
else:
    print(f'{n} is not a armstrong number.')