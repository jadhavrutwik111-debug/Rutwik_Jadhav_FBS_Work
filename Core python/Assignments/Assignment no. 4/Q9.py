#print all numbers in a range divisible by given number
num = int(input('Enter the number to find the multiple of number: '))
start = int(input('Enter the start of range: '))
stop = int(input('Enter the stop of range: '))

print(f'These are the numbers divisible by {num} in given range: ')
for i in range(start,stop):
    if(i % num == 0):
        print(i)