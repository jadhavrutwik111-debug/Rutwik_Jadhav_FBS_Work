#minimum number of notes
#take input for amount
amt = int(input('Enter the amount: '))

#perform operation
th_2 = amt // 2000
amt = amt % 2000

hr_5 = amt // 500
amt = amt % 500

hr_2 = amt // 200
amt = amt % 200

hr_1 = amt // 100
amt = amt % 100

ru_50 = amt // 50
amt = amt % 50 

ru_20 = amt // 20
amt = amt % 20

ru_10 = amt // 10
amt = amt % 10

minimum_notes = th_2 + hr_5 + hr_2 + hr_1 + ru_50 + ru_20 + ru_10

#display result 
print(f'The minimun required notes are: {minimum_notes}.')
      