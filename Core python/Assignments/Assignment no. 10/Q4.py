def reverseList(li):
    i = 0
    j = len(li) - 1
    
    while(i < j):
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1
        
li = [10, 30, 40, 50, 100, 60, 70, 20, 80, 90]
reverseList(li)
print(li)
