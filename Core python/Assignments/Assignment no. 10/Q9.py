def separateOddEven(li, odd_li, even_li):
    n = len(li)
    for i in range(0, n):
        if(li[i] % 2 == 0):
            even_li.append(li[i])
        else:
            odd_li.append(li[i])

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_li = []
even_li = []
separateOddEven(li, odd_li, even_li)
print('Odd element list:', odd_li)
print('Even element list:', even_li)