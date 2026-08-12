def linearSearch(li, val):
    size = len(li)
    count = 0
    for i in range(0, size - 1):
        if(li[i] == val):
            count += 1
    return count

li = [20, 56, 10, 80, 95, 10, 20, 48, 70, 60, 10]
val = int(input('Enter the value to be search in list: '))

res = linearSearch(li, val)
if(res > 0):
    print(f'{val} is present {res} number of times in the list.')
else:
    print(f'{val} is not present in the list.')