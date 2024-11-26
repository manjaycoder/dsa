class Car:
    totalCar=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.totalCar+=1

    def FullName(self):
        return f"{self.__brand}{self.__model}"
    def get_brand(self):
        return self.__brand + '!'
    def FuelType(self):
        return 'Petrol or diesel'
    @staticmethod
    def Vihecle():
        return 'Cars is amazing vehicles'
    @property
    def model(self):
        return self.__model


class ElectronicCar(Car):
    def __init__(self,__brand,model,batterysize):
        super().__init__(__brand,model)
        self.batterysize=batterysize
    def FuelType(self):
        return "Electorical"
    
C1=Car('Moto','Moto one action')
print(isinstance(C1,Car))
print(isinstance(C1,ElectronicCar))
















# c1=Car('tata','motor')
# print(c1.FullName())