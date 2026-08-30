str = input('Enter the string: ')
res = ''
for ch in  str:
    if(ch == ' '):
        res += '-'
    else:
        res += ch

print(res)