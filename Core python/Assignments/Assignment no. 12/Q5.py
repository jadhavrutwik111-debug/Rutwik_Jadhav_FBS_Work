str = input('Enter the string: ')
c = 0
for ch in str:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):

        c += 1

print('Total number of vowels is: ', c)