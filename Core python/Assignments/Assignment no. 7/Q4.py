for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ', end = ' ')

    for j in range(1, i + 1):
        print(i + j - 1, end = ' ')

    for j in range(1, i):
        if(j == 1):
            print(2 * (i - 1), end = ' ')
        else:
            print(2 * (i - 1) - j + 1, end = ' ')
    print()
