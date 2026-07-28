user_id = 'Rutwik'
password = 'Rutwik@123'

for i in range(1, 4):
    user = input('Enter the user name: ')
    paswd = input('Enter the password: ')

    if(user == user_id and paswd == password):
        print('User is varified')
        break
    elif(i <= 2):
        print('Re-enter the user name and password: ')
    else:
        print('Something went wrong!!')
    