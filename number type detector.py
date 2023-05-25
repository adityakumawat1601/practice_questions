#1.	Write a Python program to check whether a number is negative, positive or zero.

num = int(input("enter a number:"))

if num<0:
    print("this is a negative number")
elif num == 0:
    print("this is zero")
elif num > 0:
    print("this is a positive number")