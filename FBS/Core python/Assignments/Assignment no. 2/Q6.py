#calculate total salary
#take input for basic ammount
basic = int(input('Enter the basic salary of employee: '))
da = 10
ta = 12
hra = 15

#claculate total salary
da_amt = basic * (da / 100)
ta_amt = basic * (ta / 100)
hra_amt = basic * (hra / 100)

total_salary = basic + da_amt + ta_amt + hra_amt

#display result
print(f'Total salary of employee is: {total_salary}.')
