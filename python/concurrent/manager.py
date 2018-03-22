#!/usr/bin/env python3

'''
multiprocess study
'''
from multiprocessing import Queue
import time
import os
from worker import Worker

class WorkerManager():
    """
    WokerManager is used to manage the workers including:
    1. alloc_workers
    2. start_workers
    3. stop_workers
    4. exec_primary_task
    """
    def __init__(self):
        self.worker_list = []
        self.task_q = Queue()
        self.running = 1

    def alloc_workers(self, total_workers, target=None, task_q=None, *args):
        """
        Alloc number workers
        """
        print('TaskManager.alloc_workers')
        for i in range(1, total_workers + 1):
            wk = Worker(i, target, task_q, *args)
            self.worker_list.append(wk)

    def start_workers(self):
        print('TaskManager.start_workers')
        [wk.start() for wk in self.worker_list]

    def stop_workers(self):
        print('TaskManager.stop_workers')
        [wk.stop() for wk in self.worker_list]
        [wk.join() for wk in self.worker_list]

    def run(self):
        try:
            while self.running:
                time.sleep(1)
        except StopException:
            self.stop_workers()
        except Exception as e:
            print(str(e))

    def stop(self):
        raise StopException('stop')

    def exec_primary_task(self, task_func, *task_args):
        """
        Put the primary task into the cmd_queue to let the worker
        execute the primary task.
        """
        print('TaskManager.primary_task {}'.format(task_args))
        [w.primary_task(task_func,*task_args) for w in self.worker_list]

