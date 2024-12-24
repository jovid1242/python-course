import datetime

class Car:
    def __init__(self, model, year, mileage): 
        self.model = model
        self._year = year
        self.__mileage = mileage

    @property
    def model(self): 
        return self._model

    @model.setter
    def model(self, value): 
        if not value:
            raise ValueError("Модель автомобиля не может быть пустой.")
        self._model = value

    @property
    def year(self): 
        return self._year

    @year.setter
    def year(self, value): 
        current_year = datetime.datetime.now().year
        if value < 1886 or value > current_year:
            raise ValueError(f"Год выпуска должен быть между 1886 и {current_year}.")
        self._year = value

    @property
    def mileage(self): 
        return self.__mileage

    @mileage.setter
    def mileage(self, value): 
        if value < 0:
            raise ValueError("Пробег не может быть отрицательным.")
        self.__mileage = value

 
car = Car("Tesla", 2020, 15000) 

print(car.model)    
print(car.year)    
print(car.mileage)   
 
try:
    car.year = 1800   
except ValueError as e:
    print(e)

try:
    car.mileage = -500   
except ValueError as e:
    print(e)