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
        
if __name__ =="__main__":
    for item in range(101):
        if prime(item):
            print(item)

        
        
