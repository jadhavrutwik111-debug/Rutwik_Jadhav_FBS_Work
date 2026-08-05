def factorial(n):
    if(n > 0):
        return n * factorial(n - 1)
    else:
        return 1

n = int(input('Enter the number to find factorial: '))
fact = factorial(n)
print(f'The factorial of {n} is {fact}')