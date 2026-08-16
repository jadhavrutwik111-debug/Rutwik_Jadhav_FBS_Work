def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / factorial(i)
    return sum

n = int(input('Enter the number: '))
sum = sumOfSeries(n)
print('Sum of series is:', sum)