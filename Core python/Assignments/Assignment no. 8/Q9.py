def palindrome(n):
    temp = n
    rev = 0
    while(temp > 0):
        d = temp % 10
        temp //= 10
        rev = rev * 10 + d

    if(n == rev):
        print(f'The {n} is a palindrome number')
    else:
        print(f'The {n} is not a palindrome number')

n = int(input('Enter the number: '))
palindrome(n)