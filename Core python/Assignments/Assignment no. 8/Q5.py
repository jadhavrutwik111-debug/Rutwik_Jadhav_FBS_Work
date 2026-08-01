def prime(a):
    if(a > 1):
        for i in range(2, a // 2 + 1):
            if(a % i == 0):
                return 0            
        else:
            return a
    return 0

def sumPrime(n):
    sum = 0
    for i in range(1, n + 1):
         sum += prime(i)

    return sum

n = int(input('Enter the number: '))

sum = sumPrime(n)

print(f'Sum of prime numbers is {sum}')

    
