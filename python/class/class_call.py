#!/usr/bin/env python3

# test __call__ function in Class


class Car():
    def __init__(self, brand, seats, engine_size):
        print("Car __init__")
        self.brand = brand
        self.seats = seats
        self.engine_size = engine_size

    def get_info(self):
        print(type(self))
        print("Car's get_info is invoked")
        return ('{}-{}seats-with {} engine size'.format(self.brand, self.seats, self.engine_size))

    def __call__(self):
        print("Car's call function")

    def __del__(self):
        print('Exist Car class, {}'.format(self.brand))


class SUVCar(Car):
    def __init__(self, brand, seats, engine_size, if_4wd):
        print("SUVCar __init__")
        self.if_4wd = if_4wd
        super().__init__(brand, seats, engine_size)

    def get_info(self):
        info = super().get_info()
        print(super().__dict__)
        print(vars(super()))
        return 'CRV : {} -- support 4wd:{}'.format(info, self.if_4wd)

    def __del__(self):
        super().__del__()
        print('Exist SUVCar class, {}'.format(self.brand))


print("Start from here")
crv = SUVCar('honda', '5', '2.4', True)
hrv = SUVCar('toyota', '5', '2.4', True)
print("Prepare call get_info")
print(crv.get_info())
