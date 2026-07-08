#take input for five subject marks
s1 = int(input('Enter marks for subject 1: '))
s2 = int(input('Enter marks for subject 2: '))
s3 = int(input('Enter marks for subject 3: '))
s4 = int(input('Enter marks for subject 4: '))
s5 = int(input('Enter marks for subject 5: '))

#calculate total marks
total_marks = s1 + s2 + s3 + s4 + s5

#calculate percentage
percentage = (total_marks / 500) * 100

#display total marks and percentage
print('Percentage:', percentage)
