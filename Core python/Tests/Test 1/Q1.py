def perimeter(l, b, r):
    return 2 * l + b + 3.14 * r

l = int(input('Enter the length: '))
b = int(input('Enter the breadth: '))
r = int(input('Enter the radius: '))
peri = perimeter(l, b, r)
print('Perimeter of given figure is:', peri)