#!/usr/bin/env python3

'''
multiprocess study
'''
from multiprocessing import Queue
import datetime
import time
import os
import signal
from manager import WorkerManager
from enum import Enum
from taskctl import TaskCtlWorker


class TaskState(Enum):
    START = 1
    STOP = 2
    CONTINUE = 3


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


class StopException(Exception):
    def __init__(self, error=None):
        self.error = error

    def __str__(self):
        return self.error if self.error is not None else 'stop_exception'


def new_task_func(num, *args):
    print('worker_{} invoke new_task_func {}'.format(num, args))


def print_fun(num, *args):
    # pass
    print('worker_{} invoke print_fun {}'.format(num, *args))


def create_kill_script():
    with open('kill.sh', 'w') as f:
        f.write('echo "kill {}"\n'.format(os.getpid()))
        f.write('kill {}'.format(os.getpid()))


def sig_handle(signum, frame):
    if signum == signal.SIGQUIT:
        print("Receive SIGQUIT")
        raise StopException()
    elif signum == signal.SIGINT:
        print("Receive SIGINT")
        raise StopException()
    elif signum == signal.SIGTERM:
        print("Receive SIGTERM")
        raise StopException()
    elif signum == signal.SIGALRM:
        print("Receive SIGALRM")
        raise TimeOut.Timeout_Exception()


def get_task_state():
    """
    This function return the task should be done.

    """
    gmt1 = time.localtime(time.time())
    if gmt1.tm_hour > 23:
        return TaskState.STOP
    elif gmt1.tm_hour == 0 and gmt1.tm_min >= 30:
        return TaskState.START
    elif gmt1.tm_hour == 15 and gmt1.tm_min >= 4:
        return TaskState.START
    else:
        return TaskState.CONTINUE


def main():
    print('Enter the main function')

    create_kill_script()

    signal.signal(signal.SIGINT, sig_handle)
    signal.signal(signal.SIGTERM, sig_handle)
    signal.signal(signal.SIGQUIT, sig_handle)
    signal.signal(signal.SIGALRM, sig_handle)
    task_q = Queue()

    wk_manager = WorkerManager()
    wk_manager.alloc_workers(10, target=print_fun, task_q=task_q)
    # for num in range(1, 5):
    #     wk = Worker(num, print_fun, task_q, 1, 2, 3)
    #     worker_list.append(wk)

    [task_q.put(x) for x in range(1, 4)]

    wk_manager.start_workers()

    task_worker = TaskCtlWorker(0, None, task_q)

    task_worker.start()

    try:
        while(1):
            # wk_manager.exec_primary_task(new_task_func, *[1, 2, 3, 4])
            time.sleep(5)
            # time.sleep(5)
            # task_state = get_task_state()
            # print(task_state)
            [task_q.put(x) for x in range(1, 10)]
    except StopException:
        print("Go into StopException")
    except TimeOut.Timeout_Exception:
        print('current time is {}'.format(time.localtime(time.time())))
    except Exception as e:
        print(e)
    finally:
        wk_manager.stop_workers()
        task_worker.stop()
        task_worker.join()

    # [w.stop() for w in worker_list]

    # [w.join() for w in worker_list]

    print('Exist the main function')


if __name__ == '__main__':
    main()


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
