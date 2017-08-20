#!/usr/bin/env python3

'''
threading study

Functions:
-------------------
    active_count : Return the number of Thread objects currently alive.
    currentThread: Return the current Thread object, corresponding to the caller’s thread of control.
    current_thread
    enumerate: Return a list of all Thread objects currently alive.
    get_ident: Return the ‘thread identifier’ of the current thread. This is a nonzero integer.
    local
    main_thread: Return the main Thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started.
    setprofile: Set a profile function for all threads started from the threading module. The func will be passed to sys.setprofile() for each thread, before its run() method is called.
    settrace: Set a trace function for all threads started from the threading module. The func will be passed to sys.settrace() for each thread, before its run() method is called.
    stack_size

Constant:
-------------------
    TIMEOUT_MAX:The maximum value allowed for the timeout parameter of blocking functions (Lock.acquire(), RLock.acquire(), Condition.wait(), etc.). Specifying a timeout greater than this value will raise an OverflowError.

Thread(class):
-------------------
    init():
        target: callable object
        name: thread name
        args: argument tuple ()
        kwargs: argument as dictionary {}
        daemon: If not None, daemon explicitly sets whether the thread is daemonic. If None (the default), the daemonic property is inherited from the current thread.

    start():

    run(): invoke the callable object. Can be override by subclass.

    join(timeout=None): Wait until thread terminates. Always return None. Should you is_alive() to judge whether the thread terminate or just join time out.

    name: A string used to identify the thread.

    is_alive(): This method returns True just before the run() method starts until just after the run() method terminates.


Lock(class):
-------------------
    2 stats: locked or unlocked

    acquire(blocking=True, timeout=-1):
        return True if get the lock and locked ths state.
        return False means failed to get the lock.
        If blocking is True the caller will be blocked if the lock state being locked until timeout.

    release():
        Release a lock.

RLock(class):
-------------------
    A reentrant lock.
'''
import threading
import time
import queue
from queue import Queue


class StopMarker:
    """This is used as an individual stopper item."""

stopper = StopMarker()


def worker(name, value, q):
    print('worker_{} start up'.format(name))

    while(value > 0):
        time.sleep(2)
        try:
            item = q.get(block=False, timeout=1.0)
            if item is stopper:
                print('worker_{} recevied stopper'.format(name))
                break
        except queue.Empty:
            print('worker_{} get queue is null'.format(name))
            pass
        except Exception as e:
            print(e)
            break

        print('worker_{} value is {}'.format(name, value))
        value -= 1

    print('worker_{} exit'.format(name))

print('Start the main function')
thread_list = []
q = Queue()

for num in range(1, 5):
    thread_list.append(threading.Thread(target=worker, args=(num, 5, q)))

[x.start() for x in thread_list]


time.sleep(3)
q.put(stopper)
time.sleep(1)
q.put(stopper)
time.sleep(1)
q.put(stopper)

[x.join() for x in thread_list]

print('Exist the main function')
# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
