class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.adometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage"""
        print(f"This car has {self.adometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric cars"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
