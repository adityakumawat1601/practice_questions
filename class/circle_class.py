class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __str__(self):
        return "circle class in mainscope , use to get area and circumference of circle"
    def get_area(self):
        area = 3.14*(self.radius)**2
        return round(area,2)
    def get_circumference(self):
        circum = 2*3.14*(self.radius)
        return round(circum,2)
