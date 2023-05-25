""" this module count.py , it count the 
no. of object made.
class --> class person make person class object 
          as attach name data to object.
it contains contructor and destructor.(del)
"""

class Person:
    """made object of person class . and count their number
             """
    count =0 #class variable available to every object
    def __init__(self,name): #constructor
        self.name = name
        Person.count +=1
    def __del__(self):
        print(f"deleting {self.name}...")
        del self
        Person.count -= 1
    def __str__(self):
        return "this is obejct of class Person"

if __name__ == "__main__":
    X  = Person("aditya")
    Y = Person("parth")
    print(f"count = {Person.count}")
    X = 100
    print(f"count = {Person.count}")


        