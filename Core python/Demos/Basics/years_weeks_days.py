#write a program to convert days into years,weeks and days

days = int(input('Enter the number of days:'))

print(id(days))
years = days // 365
#print(years)
days = days % 365
print(id(days))
weeks = days // 7
#print(weeks)
days = days % 7
#print(days)

print(f'Years: {years}, Weeks: {weeks}, Days: {days}')
