#!/usr/bin/env python3

'''
A context manager is an object that defines the runtime context to be established when executing a with statement.The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement (described in section The with statement), but can also be used by directly invoking their methods.

2 main methods:

object.__enter__(self)
----------------------
    Enter the runtime context and return either this object or another object related to the runtime context.
    The value returned by this method is bound to the identifier in the as clause of with statements using this context manager.

object.__exit__(self, exc_type, exc_value, traceback)
------------------------------------------------------
    Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.

    If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.

    Note that __exit__() methods should not reraise the passed-in exception; this is the caller’s responsibility.

The with statement
-------------------
    The with statement is used to wrap the execution of a block with methods defined by a context manager .
    This allows common try...except...finally usage patterns to be encapsulated for convenient reuse.


with A() as a, B() as b is equal to:

with A() as a:
    with B() as b:
        ...
'''

import signal
import time

# TimeOut support with statements

'''
Following is the print information
First line
Enter main
enter TimeOut __init__
Start to time
count is 10 now
count is 9 now
count is 8 now
count is 7 now
Time out
<class 'int'>
<class 'frame'>
enter Timeout_Exception __init__
Exist Timeout
go to main Timeout_Exception
Exit main function
'''

print("First line")


class TimeOut():
    class Timeout_Exception(Exception):
        def __init__(self, err="Timeout_Exception"):
            print("enter Timeout_Exception __init__")
            self.err = err

        def __str__(self):
            return self.err

    def __init__(self, sec):
        print("enter TimeOut __init__")
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


def main():
    print("Enter main")
    count = 10
    try:
        with TimeOut(5):
            while(1):
                time.sleep(1)
                print('count is {} now'.format(count))
                count -= 1
                if count <= 0:
                    break
    except TimeOut.Timeout_Exception as e:
        print("go to main Timeout_Exception")
    except MyException as e:
        print(str(e))

    print('Exit main function')


if __name__ == '__main__':
    main()
