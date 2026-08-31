li1 = [1, 2, 3, 4, 5]
li2 = [1, 3, 6, 7, 2]

li3 = []
for i in li1+li2:
    if i not in li3:
        li3.append(i)

print(li3)



