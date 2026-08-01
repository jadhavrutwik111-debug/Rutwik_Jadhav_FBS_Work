#a natural sum
def naturalSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


#factorial function
def fact(a):
    fac = 1
    for i in range(1, a + 1):
        fac *= i

    return fac

#b. factorial of natural number sum
def factSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + fact(i)

    return sum


#c. n to n power sum
def powerSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** i

    return sum


n = int(input('Enter the number: '))

sum = naturalSum(n)
res = factSum(n)
powSum = powerSum(n)

print(f'Sum of natural number series is {sum}')
print(f'Sum of factorial of numbers is {res}')
print(f'Sum of power is {powSum}')