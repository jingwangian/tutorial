#!/usr/bin/env python3


import os


class ModuleA():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'ModuleA__{}'.format(self.name)
