#!/usr/bin/env python3

'''
threading study
'''
import threading
import time
import queue
import os
from queue import Queue


class StopMarker:
    """This is used as an individual stopper item."""

stopper = StopMarker()


class Worker(threading.Thread):
    def __init__(self, num, handler,loop_times):
        """Initialize Thread object and worker."""
        threading.Thread.__init__(self)
        self.num = num #worker number
        self.running = 1
        self.handler = handler
        self.queue = Queue()
        self.stopper = StopMarker()
        self.loop_times = loop_times

    def get_cmd_queue(self):
        """Get the command from queue."""
        try:
            item = self.queue.get(block=False)
        except queue.Empty:
            item = None
        except Exception:
            item = None

        return item

    def run(self):
        print('worker_{} start to run'.format(self.num))
        while self.loop_times>0:
            print('worker_{} loop times {}'.format(self.num,self.loop_times))
            self.loop_times -=1
            try:
                item = self.get_cmd_queue()
                if item is self.stopper:
                    print('worker_{} recieved stop command'.format(self.num))
                    break
                else:
                    self.handler(self.num)
            except queue.Empty:
                print('worker_{} go into Empty'.format(self.num))
                self.handler(self.num)
            except Exception as e:
                print(e)
            finally:
                time.sleep(1)

        print('worker_{} exit from run'.format(self.num))
    def stop(self):
        """Put an item in the queue to be processed by the handler."""
        self.queue.put(self.stopper)

def print_fun(num):
    print('worker_{} invoke print_fun'.format(num))

def create_kill_script():
    with open('kill.sh', 'w') as f:
        f.write('echo "kill {}"\n'.format(os.getpid()))
        f.write('kill {}'.format(os.getpid()))

def main():
    worker_list = []

    print('Enter the main function')

    create_kill_script()

    for num in range(1,5):
        wk = Worker(num,print_fun,15)
        worker_list.append(wk)

    [w.start() for w in worker_list]

    time.sleep(7)
    [w.stop() for w in worker_list]

    [w.join() for w in worker_list]

    print('Exist the main function')


if __name__ == '__main__':
    main()


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
