def calculateSalary(bas_sal, da, ta, hra):
    return bas_sal * (da + ta + hra) / 100

n = int(input('Enter the number of employees: '))
total_salary = 0
for i in range(1, n + 1):
    basic_sal = int(input(f'Enter the salary of employee {i}: '))
    if(basic_sal < 20000):
        sal = basic_sal + calculateSalary(basic_sal, 10, 12, 15)
    else:
        sal = basic_sal + calculateSalary(basic_sal, 15, 18, 20)
    
    print(f'Total salary of employee {i} is {sal}.')
    total_salary += sal

print('Total salary of all employees is:', total_salary)