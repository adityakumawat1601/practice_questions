num = int(input("enter a number :"))
reverse = 0
while num:
    rem = num%10
    reverse = reverse*10 + rem
    num //= 10
print("reverse ",reverse)
print("double of reverse " , reverse*2)
    
    
