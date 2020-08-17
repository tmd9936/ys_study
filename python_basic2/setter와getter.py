class Car:
    def __init__(self):
        self.__horsepower = 100

    @property
    def horsepower(self):   #getter
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, str): #setter
        self.__horsepower = str

car = Car()

car.__horsepower = 300

print(car.__horsepower)