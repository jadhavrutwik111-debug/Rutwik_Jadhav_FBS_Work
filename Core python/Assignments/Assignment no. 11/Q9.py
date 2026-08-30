def cubeOfList(li, li1):
    for i in range(len(li)):
        li1.append(li[i] ** 3)

def squareOfList(li, li2):
    for i in range(len(li)):
        li2.append(li[i] ** 2)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li1 = []
li2 = []
cubeOfList(li, li1)
squareOfList(li, li2)

print('List :', li)
print('Square of list:', li2)
print('Cube of list:', li1)