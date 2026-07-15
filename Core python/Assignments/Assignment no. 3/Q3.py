#check triangle is valid or not
#take inputs of angles of triangle
a1 = int(input('Enter the first angle: '))
a2 = int(input('Enter the second angle: '))
a3 = int(input('Enter the third angle: '))

#calculate sum of angles
sum = a1 + a2 + a3

if(sum == 180):
    print('The triangle is valid.')
else:
    print('The triangle is invalid.')