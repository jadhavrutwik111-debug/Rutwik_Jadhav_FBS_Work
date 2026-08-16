for i in range(1, 6):
    for j in range(1, 6):
        if((i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0)):
            print(0, end = ' ')
        elif((i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0) ):
            print(1, end = ' ')
    print()