#!/usr/bin/env python

"""
Start multipule thread to download url from website
"""

import os
import time


class File:
    ST_NEW = 1
    ST_UPLOADING = 2
    ST_UPLOADED = 3
    ST_MOVING = 4
    ST_MOVED = 5
    ST_MOVING_FAILED = 6

    def __init__(self, ):
        # self.id = UUID() #Transaction ID
        self._rules = None
        self._state = File.ST_NEW

    @property
    def rules(self):
        print("getter")
        return self._rules

    @rules.setter
    def rules(self, value):
        print("setter")
        self._rules = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def check(self):
        print("check function")
        if self._state == self.


f = File()

f.rules = 'abc'

f.check()
