root = input("size of animal[short or tall]: ").strip().lower()

if root == "tall":
    neck = input("neck long or short: ")
    if neck == "long":
        print("girrafe.")
    elif neck == "short":
        nose = input("nose long or short:")
        if nose == "short":
            habitat = input("live on land or in water:")
            if habitat == "land":
                print("rhino")
            else:
                print("hippo")
        else:
            print("elephant.")
elif root =="short":
    squeak = input("animal can or cannot squeak:")
    if squeak == "can squeak":
        print("animal might be a rat.")
    else:
        print("animal might be a squirrel.")
    