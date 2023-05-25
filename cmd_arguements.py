'''
0 - succes 
1 - failure
'''
import sys

#system arguements contains command line arguements . automatically converted to a list.by default string
if len(sys.argv) !=3:
    print("!ERROR. three agruements required.")
    print(" like this = add.py 34 22 ")
    exit(1)
x = int(sys.argv[1])
y = int(sys.argv[2])
print(f"x = {x}")
print(f"y = {y}")
print(f"x+y = {x+y}")
sys.exit(0)

#exit is the last line of program . 0 is success . 
