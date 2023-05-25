
import random
guess = random.randint(1,50)
print("welcome to guess game.")
chance = 5
while chance>0:
    print("__"*50)
    print(f"you have {chance} chance left.".center(100,"-"))
    
    user = int(input("\nguess a number[1-50]:\n"))
    if user<1 or user>50:
        print("\nwarning ! number should be from 1 to 50.\n")
        continue
    if user == guess:
        print("\nyou are such master.you have won the game.\n ")
        break
    elif user > guess:
        print("\nyour guess is high.\n")
    else:
        print("\nyour guess is low.\n")
    chance-=1
else:
    print("\nyou are such a loser.\n")
    
    