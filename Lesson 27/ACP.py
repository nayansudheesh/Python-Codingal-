class car:
    def maxspeed_fuel(self, maxspeed , fuel):
        pass
class BMW(car):
    def maxspeed_fuel(self, maxspeed , fuel):
        self.maxspeed = maxspeed
        self.fuel = fuel
        print(f"the  fuel type  a BMW   is {fuel}   and its maxspeed is {maxspeed} km/h")
class Ferrari(car):
    def maxspeed_fuel(self, maxspeed , fuel):
        self.maxspeed = maxspeed
        self.fuel = fuel
        print(f"the  fuel type of  a ferrari   is {fuel}   and its maxspeed is {maxspeed} km/h")

c1 = BMW()
c1.maxspeed_fuel(150, "disel")
c2 = Ferrari()
c2.maxspeed_fuel(300 , "petrol")
