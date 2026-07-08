#Reverse a three digit number
#take input for three digit number
num = int(input('Enter the three digit number: '))
temp = num
rev_num = 0
#perform operation
d1 = num % 10
rev_num = rev_num * 10 + d1
num = num // 10

d2 = num % 10
rev_num = rev_num * 10 + d2
num = num // 10

d3 = num % 10
rev_num = rev_num * 10 + d3
num = num // 10

print(f'The reverse number of {temp} is {rev_num}.')