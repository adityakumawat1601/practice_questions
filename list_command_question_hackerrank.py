
n = int(input())
c =1
nums = []
while c<=n:
    command = input().lower().split()
  
    
    if command[0] == "insert":
        nums.insert(int(command[2]),int(command[1]))
        
    elif command[0] == "remove":
        nums.remove(int(command[1]))
        
    elif command[0] == "append":
        nums.append(int(command[1]))
        
    elif command[0] == "sort":
        nums.sort()
        
    elif command[0] == "pop":
        nums.pop()
        
    elif command[0] == "reverse":
        nums.reverse()
    print(nums)
    
   
    else:
        print("invalid command type,please try again.")
    c += 1
