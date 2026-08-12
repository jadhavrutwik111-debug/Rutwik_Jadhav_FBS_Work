def minimumElement(li):
    size = len(li)
    min = li[0]
    for i in range(1, size):
        if(li[i] < min):
            min = li[i]
    return min

def maximumElement(li):
    size = len(li)
    max = li[0]
    for i in range(1, size):
        if(li[i] > max):
            max = li[i]
    return max

li = [63, 78, 92, 12, 34, 76, 54, 67]
max = maximumElement(li)
print('Maximum element from list is:', max)
min = minimumElement(li)
print('Minimum element from list is:', min)