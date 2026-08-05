def reverseNumber(num, rev):
    if(num > 0):
        rev = rev * 10 + num % 10
        return reverseNumber(num // 10, rev)
    else:
        return rev

num = int(input('Enter the number: '))
res = reverseNumber(num, 0)
print(f'The reverse number of {num} is {res}')