s = input('Enter the string: ')
n = int(input('Enter the index: '))

res = ''
for i in range(len(s)):
    if(i != n):
        res += s[i]

print(res)