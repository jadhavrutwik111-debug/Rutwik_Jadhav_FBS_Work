def sortList(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - 1):
            if(li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]


li_1 = [6, 7, 8, 9, 10]
li_2 = [1, 2, 3, 4, 5]

li_1.extend(li_2)
print(li_1)

sortList(li_1)
print('Sorted list:', li_1)