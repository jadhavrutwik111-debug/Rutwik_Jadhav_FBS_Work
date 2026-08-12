def removeDuplicate(li, uni_li):
    size = len(li)
    for i in range(0, size):
        if(li[i] not in uni_li):
            uni_li.append(li[i])


li = [10, 20, 30, 10, 40, 80, 50, 10, 20, 30, 50]
uni_li = []
print('Original list:', li)
removeDuplicate(li, uni_li)
print('After removing duplicates:', uni_li)