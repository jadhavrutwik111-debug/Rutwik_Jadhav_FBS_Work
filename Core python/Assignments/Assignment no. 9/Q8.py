def checkPrime(num, a):
    if(a <= num // 2):
        if(num % a == 0):
            return 0
        return checkPrime(num, a + 1)
    else:
        return 1

num = int(input("Enter the number: "))

if(num <= 1):
    print(f'{num} is not a prime number')
else:
    res = checkPrime(num, 2)

    if(res == 0):
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")