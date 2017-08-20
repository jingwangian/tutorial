#!/usr/bin/env python3

'''
multiprocess study
'''
import multiprocessing
from multiprocessing import Process, Queue
import time
import os
import queue
import signal
from command import ProcessCommand



class Worker(Process):
    def __init__(self, worker_num, handler, task_q, *args):
        """Initialize Process object and worker."""
#         super().__init__(self,group=None)
        multiprocessing.Process.__init__(self)

        self.num = worker_num  # worker number
        self.running = 1
        self.handler = handler
        self.queue = Queue()
        self.task_q = task_q
        self.stopper = ProcessCommand()
        self.args = args

    def get_cmd_queue(self):
        """Get the command from queue."""
        try:
            item = self.queue.get_nowait()
        except queue.Empty:
            item = None
        except Exception:
            item = None

        return item

    def get_task(self):
        try:
            item = self.task_q.get_nowait()
        except queue.Empty:
            item = None
        except Exception:
            item = None

        return item

    def run(self):
        print('worker_{} start to run'.format(self.num))

        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGQUIT, signal.SIG_IGN)

        while self.running:
            try:
                item = self.get_cmd_queue()
                if item is not None:
                    if item.type == ProcessCommand.CommandType.STOP:
                        print('worker_{} recieved stop command'.format(self.num))
                        break
                    elif item.type == ProcessCommand.CommandType.TASK:
                        # print('worker_{} recieved new task'.format(self.num))
                        item.func(self.num,*item.args)
                else:
                    task_item = self.get_task()
                    if task_item is not None:
                        self.handler(self.num, task_item)
                    else:
                        time.sleep(1)
            except Exception as e:
                print(e)
            finally:
                time.sleep(1)

        print('worker_{} exit from run'.format(self.num))

    def stop(self):
        """Put an item in the queue to be processed by the handler."""
        self.queue.put(self.stopper)

    def primary_task(self, task_handle, *args):
        """
        Put primary task into the command_queue. The worker will finishe primary task
        if there is. Then continue to the regular tasks from task_q
        """
        pcmd = ProcessCommand(ProcessCommand.CommandType.TASK, task_handle,*args)
        self.queue.put(pcmd)


def main():
    pass


if __name__ == '__main__':
    main()


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
