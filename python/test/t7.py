#!/usr/bin/env python3
from abc import ABC
from abc import abstractmethod

class Foo:
    def __init__(self,index):
        self.index = index
    def __getitem__(self, index):
        pass
    def __len__(self):
        print('Foo len')
        return len(index)

    def get_iterator(self):
        print('Foo get_iterator')
        return iter(self)

class MyIterable(ABC):
    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        print('My ABC get_iterator')
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

# f = Foo([1,2,3,4])

# for x in f:
#     print(x)


def greeting(name: str) -> str:
    print(name)

greeting(1)