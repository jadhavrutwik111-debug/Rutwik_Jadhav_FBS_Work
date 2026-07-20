#factorial of a number
n = int(input('Enter the number to find factorial of it: '))

fact = 1

for i in range(1,n+1):
    fact *= i

print(f'The factorial of {n} is {fact}.')