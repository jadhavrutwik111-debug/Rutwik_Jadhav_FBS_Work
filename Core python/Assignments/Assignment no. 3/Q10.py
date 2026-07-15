#marriage eligibility of person
gender = input('Enter the gender m/f : ')
age = int(input('Enter the age: '))
if(gender == 'f'):
    if(age >= 18):
        print('The girl is eligible for marriage.')
    else:
        print('The girl is not eligible for marriage.')
else:
    if(age >= 21):
        print('The boy is eligible for marriage.')
    else:
        print('The boy is not eligible for marriage.')
        