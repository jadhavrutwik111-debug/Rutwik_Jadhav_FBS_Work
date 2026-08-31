li = [5, 7, 2, 7, 5, 2, 5]
di = {}
for i in li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

for i in di:
    if(di[i] % 2 != 0):
        print('Missing coin:', i)