class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll_no = roll
        
    def set_age(self,age):
        self.age  = age
        print("!age successfully set.")
    def set_marks(self,marks):
        self.marks = marks
        print("!marks set complete")
    def display(self):
        print("information of student-->")
        print("name--",self.name)
        print("roll number--",self.roll_no)
        print("age--",self.age)
        print("marks",self.marks)
    def __str__(self):
        return f"\tStudent({self.name}) is object of this class."
    
        
