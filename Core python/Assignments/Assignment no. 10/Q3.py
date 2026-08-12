def secondLargest(li):
    size = len(li)
    first = li[0]
    second = 0
    for i in range(1, size):
        if(li[i] > first):
            second = first
            first = li[i]
        elif(li[i] > second):
            second = li[i]
    return second

li = [12, 54, 67, 87, 23, 45, 90, 96]
second_largest = secondLargest(li)
print('The second largest element from list is:', second_largest)