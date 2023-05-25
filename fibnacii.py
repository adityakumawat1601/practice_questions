
def fib(x):
'''
this function calculates fibnacii value for given x number.
=> eg. fib(0) = 0,fib(1) = 1
fib(5) = fib(4)+fib(3)
this is solved by recursion
in this eg . for fib of 5 
upper two conditions are false. so we return the last line . in which function is calling 
function , fib(5) is calling fib(4)and fib(3) .which again calling fib(3)+fib(2) then fib(2)+fib(1
as we are given fib(1) return 1 so

fib(2) returns 1 + 0 = 1
fib(3) returns 2 +1 = 2
fib(4) returns 3+2 = 2+1 = 3
fib(5) returns fib(4) +fib(3) as we calcutated value for fib(4) is 3 and 
fib(3) is 2 . then for fib(5) is 3+2 = 5

fib(6) = fib(5)+fib(4) which is 5 + 3 respectively.
i hope you understands.


'''
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x-1)+fib(x-2)
