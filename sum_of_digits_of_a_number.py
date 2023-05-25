def sum_digits(num):
    start = 0
    while num:
        
        remainder = num%10
        start += remainder
        num = num//10
    print(start)
    
    

x = int(input())
sum_digits(x)
