x = int(input('Enter the value of x : '))
n = int(input('Enter the number terms: '))
sum = 0

for i in range(1,n + 1):
    if(i % 2 == 1):
        sum += x * i / (2 * i - 1)
    else:
        sum -= x * i / (2 * i - 1)

print(f'Sum of series is {sum}')