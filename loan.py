job_type = input("job type[private/government/business]")

if job_type == "government":
    salary = float(input("enter your monthly salary:"))
    if salary >= 50000:
        print("you are eligible for loan . congratulations!")
    else:
        print("you are not eligible.We are sorry!")

elif job_type == "business":
    turn_over = float(input("enter your yearly turn over:"))
    if turn_over >= 20000000:
        print("congrats!you are approved for loan")
    else:
        print("sorry sir you cannot get loan from our bank") 
else:
    print("not eligible")
    