
def check_digits(num):
    if num<10 and num>-10:
        return "one digit"
    elif num>=10 and num<=99:
        return "two digits"
    elif num>100 and num<=999:
        return "threee digits."
    elif num>=1000 and num<=9999:
        return "four digits"
        
  
