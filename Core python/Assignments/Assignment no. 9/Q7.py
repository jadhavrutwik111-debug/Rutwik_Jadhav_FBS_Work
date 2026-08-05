def sumOfDigits(num):
    if(num > 0):
        return num % 10 + sumOfDigits(num // 10)
    else:
        return 0

num = int(input('Enter the number: '))
sum = sumOfDigits(num)
print(f'The sum of digits of {num} is {sum}')