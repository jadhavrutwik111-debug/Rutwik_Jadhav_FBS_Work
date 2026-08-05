def fibonacci(n, a, b):
    if(n > 0):
        c = a + b
        print(c)
        a = b
        b = c
        fibonacci(n -1, a, b)

n = int(input('Enter the number to print fibonacci series: '))

fibonacci(n, -1, 1)
