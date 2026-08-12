def sumOfListElement(li, size):
    #sum = 0
    # for i in range(0, size):
    #     sum += li[i]
    # return sum
    if(size >= 0):
        return li[size] + sumOfListElement(li, size - 1)
    else:
        return 0

li = [10, 20, 30, 40, 50, 60, 70]
sum = sumOfListElement(li, len(li) - 1)
print('Sum of list element is:', sum)
