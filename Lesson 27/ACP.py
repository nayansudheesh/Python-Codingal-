class car:
    def maxspeed_fuel(self, maxspeed , fuel):
        pass
class BMW(car):
    def maxspeed_fuel(self, maxspeed , fuel):
        self.maxspeed = maxspeed
        self.fuel = fuel
        print(f"the maximum fuel a BMW can contain  is {fuel} L  and its maxspeed is {maxspeed} km/h")
class Ferrari(car):
    def maxspeed_fuel(self, maxspeed , fuel):
        self.maxspeed = maxspeed
        self.fuel = fuel
        print(f"the maximum fuel a ferrari can contain  is {fuel} L  and its maxspeed is {maxspeed} km/h")

c1 = BMW()
c1.maxspeed_fuel(150, 100)
c2 = Ferrari()
c2.maxspeed_fuel(300 , 90)
