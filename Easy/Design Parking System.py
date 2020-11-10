class ParkingSystem:

    def __init__(self, big, medium, small):
        self.lot = {1:big, 2:medium, 3:small}
        self.output = []

    def addCar(self, carType):
        if carType == 1:
            if self.lot[1] >=1:
                self.lot[1] -=1
                return True
            else:
                return False
        elif carType == 2:
            if self.lot[2] >=1:
                self.lot[2] -=1
                return True
            else:
                return False
        elif carType == 3:
            if self.lot[3] >=1:
                self.lot[3] -=1
                return True
            else:
                return False
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
