count = 0
num = 12345679000000
while num:
    count += 1
    num = num//10  #every time number will decrease by one digit.
print(count)
