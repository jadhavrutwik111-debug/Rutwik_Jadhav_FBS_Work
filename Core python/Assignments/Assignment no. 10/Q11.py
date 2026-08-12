def divisibleBy(li, m, n):
    size = len(li)
    print(f'Below numbers are divisible by {m} and {n}:')
    for i in range(0, size):
        if(li[i] % m == 0 and li[i] % n == 0):
            print(li[i])


li = [12, 34, 15, 78, 75, 30, 69, 99, 18]
m = int(input('Enter the value of m: '))
n = int(input('Enter the value of n: '))
divisibleBy(li, m, n)
