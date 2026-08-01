def reverseNumber(n):
    rev = 0
    while(n > 0):
        d = n % 10
        n //= 10
        rev = rev * 10 + d

    return rev

n = int(input('Enter the number: '))
rev = reverseNumber(n)
print(f'The reverse of {n} is {rev}')