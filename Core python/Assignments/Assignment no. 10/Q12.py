def cubeOfList(li_1, li_3, size):
    for i in range(0, size):
        li_3.append(li_1[i] ** 3)

def squareOfList(li_1, li_2, size):
    for i in range(0, size):
        li_2.append(li_1[i] ** 2)

def createSimpleList(li_1, size):
    print('Enter the element in list: ')
    for i in range(0, size):
        li_1.append(int(input()))

li_1 = []
li_2 = []
li_3 = []
size = int(input('Enter the size of list: '))
createSimpleList(li_1, size)
squareOfList(li_1, li_2, size)
cubeOfList(li_1, li_3, size)
print('List of numbers:', li_1)
print('Square of list elements:', li_2)
print('Cube of list elements:', li_3)