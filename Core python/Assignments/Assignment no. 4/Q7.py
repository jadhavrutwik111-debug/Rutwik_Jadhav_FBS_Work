#print integers upto n that aren't divisible by 2 and 3
n = int(input('Enter the number: '))

print('These are the numbers that are not divisible by 2 and 3:')

for i in range(n):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)
   