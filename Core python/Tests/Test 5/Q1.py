d = [2000, 500, 200, 100, 50, 20, 10, 5]
amt = int(input('Enter the amount: '))
nt = 0
for i in range(len(d)):
    nt = nt + amt // d[i]
    amt = amt % d[i]

print('Minimum number of notes:', nt)