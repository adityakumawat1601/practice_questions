
nums = list(map(int,input("enter numbers with single space:").split()))
visited = set()

for item in nums:
    if item in visited:
        print("first repeating character in your list of numbers:",item)
        break
    else:
        visited.add(item)
else:
    print(-1)
        
