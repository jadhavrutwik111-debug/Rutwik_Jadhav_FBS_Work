for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ', end = ' ')

    for j in range(1, i + 1):
        print(chr(j + 64), end = ' ')

    for j in range(1, i):
        print(chr(i + j + 64), end = ' ')

    print()