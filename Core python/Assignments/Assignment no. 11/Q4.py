def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - 1):
            if(li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li[-2]

li = [12, 1, 67, 45, 10, 18, 3, 2, 35, 98]
res = bubbleSort(li)
print('Second largest number from list is:', res)