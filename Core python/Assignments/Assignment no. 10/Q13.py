def removeEvenNumbers(li, odd_li):
    size = len(li)
    for i in range(0, size):
        if(li[i] % 2 != 0):
            odd_li.append(li[i])

li = [1, 3, 46, 30, 23, 67, 78, 98, 57]
odd_li = []
print('List before removing even numbers:', li)
removeEvenNumbers(li, odd_li)
print('List after removing even numbers:', odd_li)
