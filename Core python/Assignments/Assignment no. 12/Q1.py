str = input('Enter the string: ')
res = ''

for i in str:
    if(i == 'a'):
        res += '$'
    else:
        res += i
# print(str.replace('a','$'))
print(res)
