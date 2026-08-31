li = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

di = {}

for i in li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

print(di)