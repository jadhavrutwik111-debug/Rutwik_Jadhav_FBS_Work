n = int(input('Enter the number: '))
r = 2
a = 1
sum = 0
for i in range(1, n + 1):
    sum += a * r ** (n - i)
print('Sum of GP series is:',sum)