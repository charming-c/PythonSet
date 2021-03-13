class Car:
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        '''将里程表读书设置成制定的值
           禁止向里程表读数往回调'''
        if mileage < self.odometer_reading:
            print(f"you can't roll back a odometer")
            return
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car('audi','a4',2019)
my_new_car.update_odometer(23)
my_new_car.update_odometer(20)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()