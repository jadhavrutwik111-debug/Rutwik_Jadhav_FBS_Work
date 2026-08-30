s = input('Enter the string: ')
count = 0

for ch in s:
    if 'a' <= ch <= 'z':
        count += 1

print("Lowercase letters:", count)