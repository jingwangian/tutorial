#!/usr/bin/env python3


import os


class Car():
    def __init__(self, name, company_name, module, seats):
        self.name = name
        self.company_name = company_name
        self.module = module
        self.seats = seats

    def __str__(self):
        return '{}--{}--{}--{}'.format(self.name, self.company_name, self.module, self.seats)
