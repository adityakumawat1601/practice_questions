#code for calculator
n1 = float(input('value :'))
sign = input('[sign:+,-,*,**,/]:')
n2 = float(input("value :"))

if sign == '+':
    print(n1+n2)
elif sign == '-':
    print(n1-n2)
elif sign == '*' :
    print(n1*n2)
elif sign == '/':
    print(n1/n2)
elif sign == '**':
    print(n1**n2)
else:
    print("invalid")

    