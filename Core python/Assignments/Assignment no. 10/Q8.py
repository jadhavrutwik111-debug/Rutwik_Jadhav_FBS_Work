def createDuplicateList(li, dup_li):
    size = len(li)
    for i in range(0, size):
        dup_li.append(li[i])

li = [10, 30, 20, 40, 60, 80, 50]
dup_li = []
createDuplicateList(li, dup_li)
print('Original list:', li)
print('Duplicate list:', dup_li)
