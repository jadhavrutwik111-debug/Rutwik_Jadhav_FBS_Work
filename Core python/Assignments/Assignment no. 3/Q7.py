#userid and password authentication
#take input for userid and password
user_id = input('Enter the userID: ')
passwd = input('Enter the password: ')

if(user_id == 'Rutwik' and passwd == 'Rutwik@123'):
    print('User is valid')
else:
    print('User is invalid!!')