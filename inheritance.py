class Car:
    brand =""
    model =""
    year = 0
    speed = 0
    mileage = 0
#self looks within itself for attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model= model
        self.year = year

#class key word(class) Name of the class(ElectricCar)class you want to inherit from(Car)
#super helps you access attributes/implementation from the Base class
class ElectricCar(Car): 
    battery_capacity = 0
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)

    

#below not actionable need to type this and then call on it elsewhere

class CEngineCar(Car):
    engine_capacity = 0 
    car = Car()
    car.year = 2020

electric_car = ElectricCar()
electric_car.brand ="Tesla"
electric_car.year = 2008
electric_car.battery_capacity = 2000

c_engine_car = CEngineCar()
c_engine_car.brand= "Toyota Corolla"
c_engine_car.model= ("Year 2000")
print(f"CEngine car model: {c_engine_car.brand} {c_engine_car.model} ")
print(f"Electric car model: {electric_car.brand} {electric_car.year}")

# Grand child deriving attributes from the base and derived class
#class Matrix(CEngineCar): 
#     new_variable=0


# new_class = Matrix()
# new_class.engine_capacity = 0
# new_class.brand ="Matrix"


