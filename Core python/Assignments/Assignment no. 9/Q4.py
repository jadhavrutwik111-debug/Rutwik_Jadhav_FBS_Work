def sumOfNatrual(n):
    if(n > 0):
        return n + sumOfNatrual(n - 1)
    else:
        return 0

n = int(input('Enter the number: '))
sum = sumOfNatrual(n)
print(f'The sum of {n} numbers is {sum}')