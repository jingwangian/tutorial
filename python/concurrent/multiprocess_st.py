#!/usr/bin/env python3

'''
multiprocess study
'''
from multiprocessing import Queue
import time
import os
import signal
from manager import WorkerManager

class StopException(Exception):
    def __init__(self, error=None):
        self.error = error

    def __str__(self):
        return self.error if self.error is not None else 'stop_exception'


def new_task_func(num, *args):
    print('worker_{} invoke new_task_func {}'.format(num,args))


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


def main():
    print('Enter the main function')

    create_kill_script()

    signal.signal(signal.SIGINT, sig_handle)
    signal.signal(signal.SIGTERM, sig_handle)
    signal.signal(signal.SIGQUIT, sig_handle)

    task_q = Queue()

    wk_manager = WorkerManager()
    wk_manager.alloc_workers(5,target=print_fun, task_q = task_q)
    # for num in range(1, 5):
    #     wk = Worker(num, print_fun, task_q, 1, 2, 3)
    #     worker_list.append(wk)

    [task_q.put(x) for x in range(1, 500)]

    wk_manager.start_workers()

    try:
        while(1):
            time.sleep(2)
            wk_manager.exec_primary_task(new_task_func,*[1,2,3,4])
            time.sleep(3)
    except StopException:
        print("Go into StopException")
        wk_manager.stop_workers()

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
