#check triangle is valid or not
#take input for three sides of triangle
s1 = int(input('Enter the first side of a triangle: '))
s2 = int(input('Enter the second side of a triangle: '))
s3 = int(input('Enter the third side of a triangle: '))

if(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 ):
    print('Triangle is valid.')
else:
    print('Invalid triangle!')