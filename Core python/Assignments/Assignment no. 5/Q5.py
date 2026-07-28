#print prime numbers between 1 to 100
for i in range(2, 100):
    if(i > 1):
        for j in range(2, i // 2 + 1):
            if(i % j == 0):
                break
        else:
            print(i)
  