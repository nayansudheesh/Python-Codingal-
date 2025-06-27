class vehicle:
    #defining init
    def __init__(self, max_speed , mileage):


         self.max_speed = max_speed
         self.mileage = mileage
model1X = vehicle(240, 18)
print("model max speed" , model1X.max_speed)
print("model mileage" , model1X.mileage)