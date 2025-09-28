class veicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(veicle):
    def fare(self):
        total_fare = super().fare()
        total_fare += total_fare * 0.10
        return total_fare

my_bus = Bus(50)
print("Total Bus Fare:", my_bus.fare())
