def sum_digits(num):
    
    if num!=0:
        remainder = num%10
        sum_digits(num//10)
        print(remainder)

x = int(input())

sum_digits(x)
