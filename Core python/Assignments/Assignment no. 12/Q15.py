s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')

c1 = 0
c2 = 0

for ch in s1:
    c1 += 1
for ch in s2:
    c2 += 1

if(c1 >= c2):
    print('Larger string is:', s1)
else:
    print('Larger string is:', s2)