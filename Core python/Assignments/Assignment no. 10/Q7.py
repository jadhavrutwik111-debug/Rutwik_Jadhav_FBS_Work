def cubeOfElement(li):
    size = len(li)
    for i in range(0, size):
        li[i] = li[i] ** 3

li = [1, 2, 3, 4, 5, 6, 7, 8]
cubeOfElement(li)
print(li)