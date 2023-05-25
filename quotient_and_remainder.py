def quotient(num1,num2):
    return num1/num2

def remainder(num1,num2):
    return num1%num2
if __name__ == "__main__":
    while True:
    
            try:
                value1 = float(input())
                value2 = float(input())
                

            except ValueError:
                print("invalid number try again")
            else:
                print(f"quotient is {quotient(value1,value2):.2f}")
                print("remainder is ",remainder(value1,value2))
                break
            finally:
                print("Thankyou")

