def areaRectangle(l, b):
    return l * b

l = int(input('Enter the length of rectangle: '))
b = int(input('Enter the breadth of rectangle: '))

area = areaRectangle(l, b)

print(f'The area of rectangle is {area}')
