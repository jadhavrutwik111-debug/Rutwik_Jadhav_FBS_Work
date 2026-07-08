x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

print(f'Before swapping: x = {x}, y = {y}')

#x, y = y, x
x = x + y
y = x - y
x = x - y

print(f'After swapping: x = {x}, y = {y}')
