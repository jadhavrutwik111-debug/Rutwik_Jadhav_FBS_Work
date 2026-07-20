#check perfect number
#perfect number means sum of proper divisors except itself is equal to that number

num = int(input('Enter the number: '))
sum = 1

for i in range(2, num // 2 + 1):
    if(num % i == 0):
        sum += i

if(sum == num):
    print(f'The {num} is a perfect number.')
else:
    print(f'The {num} is not a perfect number.')