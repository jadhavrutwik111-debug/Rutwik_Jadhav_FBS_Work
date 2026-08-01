def checkLeapYear(y):
    if(y % 4 == 0):
        print(f'The {y} is a leap year')
    else:
        print(f'The {y} is not a leap year')

y = int(input('Enter the year to check leap or not: '))

checkLeapYear(y)