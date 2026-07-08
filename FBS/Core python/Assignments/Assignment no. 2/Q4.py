#calculate area of triangle and rectangle
#take input for base,height,length and breadth
base = int(input('Enter the base of triangle: '))
height = int(input('Enter the height of triangle: '))
l = int(input('Enter the length of rectangle: '))
b = int(input('Enter the breadth of rectangle: '))

#calculate area of triangle and rectangle
area_tri = 1 / 2 * base * height
area_rect = l * b

#display result 
print('Area of triangle is:',area_tri)
print('Area of rectangle is:', area_rect)