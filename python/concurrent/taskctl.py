#!/usr/bin/env python3

'''
multiprocess study
'''
import time
import os
import signal
from worker import Worker
from command import ProcessCommand

class TaskCtlWorker(Worker):
    name = "task_controler"

    def run(self):
        print('worker_{} start to run'.format(self.name))

        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGQUIT, signal.SIG_IGN)

        while self.running:
            try:
                item = self.get_cmd_queue()
                if item is not None:
                    if item.type == ProcessCommand.CommandType.STOP:
                        print('worker_{} recieved stop command'.format(self.name))
                        break
                else:
                    time.sleep(5)
                    print("{} put task into task_q".format(self.name))
                    [self.task_q.put(x) for x in range(1,11)]
            except Exception as e:
                print(e)
            finally:
                time.sleep(1)

        print('worker_{} exit from run'.format(self.name))


def get_route_task():
    """
    Get a route task from the task_center.
    This function will send a request to the task_center and
    get a RESTFul API as following:
    {"route_id":1}
    """

def create_tasks_by_routeid():
    pass

def main():
    pass


if __name__ == '__main__':
    main()


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
