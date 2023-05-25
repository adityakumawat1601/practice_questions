
#this is code for finding minimum or max. number.

nums = [19,-22,42,55,33,79,90,10,31,11]

mi = nums[0] #here we are assuming minimum is first number in the list .

for item in nums:
    if item < mi:  #we check if the item in the list is less than mi or not .
        mi = item   #if yes than we assign new value to the mi variable .this will continue till all the items are checked . 
print('MINIMUM NUMBER IS :',mi)
    

