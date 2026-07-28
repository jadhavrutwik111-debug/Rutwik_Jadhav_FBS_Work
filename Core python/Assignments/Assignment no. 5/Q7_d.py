a = int(input('Enter the value for a : '))
s = 0
for i in range(1, 11):
    s += a * i // i

print(s)