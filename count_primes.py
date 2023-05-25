num1 = int(input())
num2 = int(input())
def prime(num):
    if num<=1:
        return 0
    elif num in [2,3,5,7,11]:
        return 1
    elif num%2==0:
        return 0
    for check in range(2,num//2):
        if num%check==0:
            return 0
    return 1
print("these are prime number between ",num1,"and",num2,":")
count = 0
for num in range(num1,num2+1):
    if prime(num):
        print(num,end = " ")
        count += 1
        
    
print(f"\ntotal prime numbers betweeen {num1,num2} are {count}")
        
