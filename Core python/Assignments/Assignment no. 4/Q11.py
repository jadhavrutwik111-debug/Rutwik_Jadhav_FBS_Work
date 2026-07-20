#check strong number
#sum of factorial of digits of number is equal to number 
num = int(input('Enter the number: '))
temp = num
fact_sum = 0

while(num > 0):
    d = num % 10
    num = num // 10
    fact = 1
    for i in range(1,d+1):
        fact *= i
    fact_sum += fact
if(temp == fact_sum):
    print(f'{temp} is a strong number.')
else:
    print(f'{temp} is not a strong number.')