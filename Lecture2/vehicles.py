class Vehicle:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

class Car(Vehicle):
    def __init__(self, make, model, year, num_wheels, num_doors):
        super().__init__(make, model, year)
        self._num_wheels = num_wheels
        self._num_doors = num_doors

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def num_doors(self):
        return self._num_doors

class ElectricCar(Car):
    def __init__(self, make, model, year, num_wheels, num_doors, battery_size, charge_time):
        super().__init__(make, model, year, num_wheels, num_doors)
        self._battery_size = battery_size
        self._charge_time = charge_time

    @property
    def battery_size(self):
        return self._battery_size

    @property
    def charge_time(self):
        return self._charge_time

# Example usage:
vehicle = Vehicle("Toyota", "Camry", 2023)
print("Vehicle Make:", vehicle.make)
print("Vehicle Model:", vehicle.model)
print("Vehicle Year:", vehicle.year)

car = Car("Honda", "Civic", 2022, 4, 4)
print("Car Make:", car.make)
print("Car Model:", car.model)
print("Car Year:", car.year)
print("Car Number of Wheels:", car.num_wheels)
print("Car Number of Doors:", car.num_doors)

electric_car = ElectricCar("Tesla", "Model S", 2023, 4, 4, "100 kWh", "6 hours")
print("Electric Car Make:", electric_car.make)
print("Electric Car Model:", electric_car.model)
print("Electric Car Year:", electric_car.year)
print("Electric Car Number of Wheels:", electric_car.num_wheels)
print("Electric Car Number of Doors:", electric_car.num_doors)
print("Electric Car Battery Size:", electric_car.battery_size)
print("Electric Car Charge Time:", electric_car.charge_time)