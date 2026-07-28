#print armstrong number in the given range
start = int(input('Enter the start of range: '))
stop = int(input('Enter the stop of range: '))

for i in range(start, stop + 1):
    a = len(str(i))
    temp = i
    sum = 0
    while(temp > 0):
        d = temp % 10
        sum = sum + d ** a
        temp = temp // 10
    if(sum == i):
        print(i)
    
