str = input('Enter the string: ')
wc = 1
c = 0

for ch in str:
    if(ch != ' '):
        c += 1
    else:
        wc += 1

print('Word count:', wc)
print('Character count:', c)