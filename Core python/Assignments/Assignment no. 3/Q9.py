#calculate grade using students marks
#take inputs for five subjects
s1 = int(input('Enter marks of first subject: '))
s2 = int(input('Enter marks of second subject: '))
s3 = int(input('Enter marks of third subject: '))
s4 = int(input('Enter marks of fourth subject: '))
s5 = int(input('Enter marks of fifth subject: '))

#calculate percentage
sum = s1 + s2 + s3 + s4 + s5
perc = sum / 5
print(perc)

#calculate grade
if(perc >= 35):
    if(perc > 40):
        if(perc > 50):
            if(perc > 60):
                if(perc > 70):
                    if(perc > 80):
                        if(perc > 90):
                            if(perc <= 100):
                                print('Grade is: A+')
                        else:
                            print('Grade is: A')
                    else:
                        print('Grade is: B+')
                else:
                    print('Grade is: B')
            else:
                print('Grade is: C+')
        else:
            print('Grade is: C')
    else:
        print('Grade is: D')
else:
    print('Student is failed!')