#convert time into seconds
#take inputs for hours,minutes and seconds
hr = int(input('Enter the hours: '))
min = int(input('Enter the minutes: '))
sec = int(input('Enter the seconds: '))

#Calculate total seconds
total_sec = hr * 60 * 60 + min * 60 + sec

#display result
print(f'After convertion total seconds is: {total_sec}.')