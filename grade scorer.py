print("**each subject maximum marks is 100")
phy = int(input("enter physics marks:"))
chem= int(input("enter chemistry marks:"))
bio= int(input("enter biology marks:"))
math=  int(input("enter mathematics marks:"))
comp = int(input("enter computer marks:"))

total_marks = phy+chem+bio+math+comp
max_marks = 500
percentage = (total_marks/500)*100
print(f"you have {percentage}% marks obtained in exams.")

if percentage >= 90:
    print("you got A grade")
elif (percentage <= 90) and (percentage >= 80) :
    print("you got B grade.")
elif (percentage <= 80) and (percentage >= 70):
    print("c grade")
elif (percentage <= 70) and (percentage >= 60):
    print("you got D grade")
elif (percentage <= 60) and (percentage >= 40):
    print("you scored E. work hard ")
else:
    print("you got F grade. you failed the test.")