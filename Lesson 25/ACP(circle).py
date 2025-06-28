class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = 3.14*(self.radius*self.radius)
        print("Area (in cm) is" , area)
    def circumference(self):
        perimeter = 2*3.14*self.radius
        print("Circumference of a circle(perimeter) is " , perimeter)
radius = int(input("Enter radius in cm"))
c = circle(radius)
c.area()
c.circumference()
