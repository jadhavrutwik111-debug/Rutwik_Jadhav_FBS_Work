#divisible by 7 and multiple of 5 in given range
start = int(input('Enter the start of range: '))
stop = int(input('Enter the stop of range: '))

print('these are the numbers divisible by 7 and multiple of 5 in given range: ')
for i in range(start,stop):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)