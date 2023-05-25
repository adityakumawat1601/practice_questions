class Temperature:
    def __init__(self,temp):
        self.temp = temp
    def __str__(self):
        return "class temperature converts fahrenheit into celsius and viceversa"
    def convert_to_Fahrenheit(self):
        F = (9*self.temp/5)+32
        return round(F,1)
        
    def convert_to_Celsius(self):
        C = 5/9*(self.temp-32)
        return round(C,1)
