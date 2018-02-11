#!/usr/bin/env python3


import os
import sys

print('car__init path:', sys.path)


from .car import Car

__all__ = ['Car', ]


def main():
    car1 = Car('civil', 'honda', 'hatch back', 5)

    print(car1)


if __name__ == '__main__':
    main()
