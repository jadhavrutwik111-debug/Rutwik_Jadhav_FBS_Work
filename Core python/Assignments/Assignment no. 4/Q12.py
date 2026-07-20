#Armstrong number
num = input('Enter the number: ')
a = len(num)
num = int(num)
temp = num
sum = 0

while(num > 0):
    d = num % 10
    sum = sum + d ** a
    num = num // 10
if(temp == sum):
    print(f'{temp} is a armstrong number.')
else:
    print(f'{temp} is not a armstrong number.')
