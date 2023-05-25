import time
for i in range(12):
    if i == 1:
        print("hi aditya how are you ?".ljust(20))
        time.sleep(1)
    elif i ==2:
        print("i am fine how about you?".rjust(70))
        time.sleep(1)
   
    elif i == 3:
        print(f"{'i am fine':<20}")
        time.sleep(1)
    elif i == 4:
        print(f"{'how about you?':>70}")
        time.sleep(1)
    elif i == 5:
        print(f"{'all good'}")
        time.sleep(1)
    elif i == 6:
        print(f"{'anyways anything new happens?'}")
        time.sleep(1)
    elif i == 7:
        print(f"{'nothing all same as before.':>70}")
        time.sleep(1)
    elif i ==8:
        print("bye bye")
    elif i == 9:
        print(f"{'tata tata':>70}")
        
    else:
        pass
