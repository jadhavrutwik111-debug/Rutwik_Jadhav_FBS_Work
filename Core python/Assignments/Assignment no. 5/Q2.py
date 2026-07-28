n = int(input('Enter the number of students: '))
avg_per = 0
for i in range(1,n+1):
    print(f'Enter the marks for student {i} =>')
    sum_marks = 0
    perc = 0
    for j in range(1,6):
        marks = int(input(f'Enter the mark of subject{j}: '))
        sum_marks += marks
    perc = sum_marks / 5
    print(f'Percentage of student{i} is {perc}')
    avg_per += perc

avg_per = avg_per / n

print(f'The average percentage of all students is {avg_per}')
