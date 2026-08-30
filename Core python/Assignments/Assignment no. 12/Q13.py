s = input('Enter the string: ')
digits = 0
letters = 0

for ch in s:
    if '0' <= ch <= '9':
        digits += 1
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letters += 1

print("Digits:", digits)
print("Letters:", letters)