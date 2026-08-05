def factorial(n):
    if(n > 0):
        return n * factorial(n - 1)
    else:
        return 1

def sumFactorial(n):
    
    if(n > 0):
        
        return factorial(n) + sumFactorial(n-1)
    else:
        return 0

n = int(input('Enter the number: '))

res = sumFactorial(n)
print('Sum of factorial is', res)