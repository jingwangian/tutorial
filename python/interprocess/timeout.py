#!/usr/bin/env python3

import signal


class TimeOut():
    class Timeout_Exception(Exception):
        def __init__(self, err="Timeout_Exception"):
            self.err = err

        def __str__(self):
            return self.err

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        print('Start to time')
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        # signal.alarm(0)
        print('Exist Timeout')
        # [print(type(x)) for x in args]

    def raise_timeout(self, *args):
        signal.alarm(0)  # Close the time out here
        print('Time out')
        [print(type(x)) for x in args]
        raise self.Timeout_Exception()
