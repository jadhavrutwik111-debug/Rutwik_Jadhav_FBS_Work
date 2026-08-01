def power(d, a):
    return d ** a


def powersum(n, a):
    sum = 0
    while(n > 0):
        d = n % 10
        sum += power(d, a)
        n //= 10

    return sum


def armstrong(n):
    a = len(n)
    temp = int(n)
    sum = powersum(temp, a)
    if(temp == sum):
        print(f'{temp} is a armstrong number.')
    else:
        print(f'{temp} is not a armstrong number.')

n = input('Enter the number to check armstrong number or not: ')
armstrong(n)
