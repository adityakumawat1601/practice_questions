# question=	Write a Python program to check whether a number is divisible by 5 and 11 or not.
#this is very important question because .
# in this num%5 means remainder . if remainder 0 than this condition is false. but we want this 
# condition thats why we use ==0 similar to not false. that make it true.
num = int(input("enter a number: "))

if num%5 == 0:
    print(f"{num} is divisible by 5")
    
elif num%11 == 0:
    print(f"{num} is divisible by 11")
else:
    print(f"{num} is not divisible by both 5 and 11")