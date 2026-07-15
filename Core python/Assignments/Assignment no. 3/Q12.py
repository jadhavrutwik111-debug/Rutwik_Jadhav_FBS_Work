#Palindrome number
num = int(input('Enter the number:'))
temp = num
rev = 0
rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

print(rev)

if(temp == rev):
    print('The number is palindrome.')
else:
    print('The number is not palindrome.')
