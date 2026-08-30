str = input('Enter the string: ')
res = ''

for i in range(len(str)):
    if(i % 2 == 0):
        res += str[i]

print(res)