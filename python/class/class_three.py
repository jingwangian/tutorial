#!/usr/bin/env python3

# @property


class Car():
    def __init__(self, brand, seats, engine_size):
        self.brand = brand
        self.seats = seats
        self.engine_size = engine_size

    def get_info(self):
        print(type(self))
        print("Car's get_info is invoked")
        return ('{}-{}seats-with {} engine size'.format(self.brand, self.seats, self.engine_size))


class SUVCar(Car):
    def __init__(self, brand, seats, engine_size, if_4wd):
        self.if_4wd = if_4wd
        super().__init__(brand, seats, engine_size)

    def get_info(self):
        info = super().get_info()
        print(super().__dict__)
        print(vars(super()))
        return 'CRV : {} -- support 4wd:{}'.format(info, self.if_4wd)


crv = SUVCar('honda', '5', '2.4', True)
print(crv.get_info())
