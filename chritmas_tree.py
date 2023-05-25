arr = [5,-6,2,10,-7,7,5,-6]

lwidth = abs(min(arr))
rwidth = abs(max(arr))

for value in arr:
    if value<0:
        value = abs(value)
        ls = ("*"*value).rjust(lwidth)
        row = ls+"*"+" ".ljust(rwidth)
        print(row)
    else:
        rs = ("*"*value).ljust(rwidth)
        row = " ".rjust(lwidth)+"*"+rs
        print(row)
        
        
        
        
        
        
        
        
        
        
        
