n = int(input('Enter the number of prime numbers you want: '))
i = 0
j = 2
while(i < n):
    for k in range(2, j // 2 + 1):
        if(j % k == 0):
            break
    else:
        print(j)
        i += 1
    j += 1
     