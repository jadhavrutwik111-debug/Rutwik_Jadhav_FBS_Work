#user login like captcha validation
import random

user = input('Enter the UserID: ')
passwd = input('Enter the password: ')  
captcha = random.randint(1000,9999)

if(user == 'Rutwik' and passwd == 'Rutwik@123'):
    print('captcha:', captcha)
    user_captcha = int(input('Enter the captcha: '))
    if(captcha == user_captcha):
        print('Login successful')
    else:
        print('Login failed!!')
else:
    print('Incorrect userID or Password!!')
