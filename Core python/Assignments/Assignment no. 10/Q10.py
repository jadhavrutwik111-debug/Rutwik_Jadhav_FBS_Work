def removeElement(li, ele, li1):
    size = len(li)
    for i in range(0, size):
        if(li[i] != ele):
            li1.append(li[i])

li = [10, 20, 40, 50, 10, 30, 10, 20]
print(li)
ele = int(input('Enter the element you want to remove from list: '))
li1 = []
removeElement(li, ele, li1)
print(li1)