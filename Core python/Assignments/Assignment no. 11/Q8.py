num = 1

for row in range(10):   
    if row % 2 == 0:
        for col in range(10):
            print(f"{num:3} ", end=" ")
            num += 1
    else:
        temp = num + 9
        for col in range(10):
            print(f"{temp:3} ", end=" ")
            temp -= 1
        num += 10
    print()