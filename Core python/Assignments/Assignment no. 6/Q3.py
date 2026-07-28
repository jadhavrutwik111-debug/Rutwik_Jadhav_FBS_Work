for i in range(1, 5):
    for j in range(1, 5 - i):
        print(' ', end = ' ')

    s = 1
    for j in range(1, i + 1):
        print(f'{s}  ', end = ' ')
        s = s * (i - j) // j
    print()