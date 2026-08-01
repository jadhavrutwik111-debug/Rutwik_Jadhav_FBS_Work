def sumOdd(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += i

    return sum

n = int(input('Enter the number: '))
sum = sumOdd(n)

print(f'Sum of odd numbers is {sum}')