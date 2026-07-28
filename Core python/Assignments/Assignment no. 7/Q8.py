k = 8
for i in range(1, 6):
    for j in range(1, i + 1):
         print(j, end = ' ')

    for j in range(1, k):
        print(' ', end = ' ')

    k -= 2

    for j in range(1, i + 1):
        if(i != 5):
            print(i - j + 1, end = ' ')

    if(i == 5):
        for j in range(1, 5):
            print(i - j, end = ' ')
            
    print()