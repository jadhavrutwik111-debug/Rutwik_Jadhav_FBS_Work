#calculate roots of quadratic equation ax^2 + bx + c = 0
#take inputs for a , b and c
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

#perform calculation
descr = b ** 2 - 4 * a * c

x1 = (-b + descr ** (1/2)) / 2 * a 
x2 = (-b - descr ** (1/2)) / 2 * a

print(f'Roots of quadratic equation are x1: {x1} and x2: {x2}')