#check type of triangle
s1 = int(input('Enter the first side: '))
s2 = int(input('Enter the second side: '))
s3 = int(input('Enter the third side: '))

if(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
    if(s1 == s2 == s3):
        print('The triangle is equilateral.')
    elif(s1 == s2 or s2 == s3 or s1 == s3):
        print('The triangle is isosceles.')
    else:
        print('The triangle is scalene.')
else:
    print('Invalid triangle!')
    