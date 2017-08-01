#!/usr/bin/env python3

'''
combinations study

Functions:
__about__,__all__,__builtins__,__cached__,__doc__,__file__,__loader__,__name__
__package__,__spec__,_heapify_max,_heappop_max,_heapreplace_max,_siftdown,_siftdown_max,_siftup
_siftup_max,
heapify,heappop,heappush,heappushpop,heapreplace,merge,nlargest
nsmallest,

heappush(heap, item)
    Push the value item onto the heap, maintaining the heap invariant.

heappop(heap)
    Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heappushpop(heap, item)
    Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

heapify(x)
    Transform list x into a heap, in-place, in linear time.

heapreplace(heap, item)
    Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

merge(*iterables, key=None, reverse=False)
    Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

nlargest(n, iterable, key=None)
    Return a list with the n largest elements from the dataset defined by iterable

nsmallest(n, iterable, key=None)
    Return a list with the n smallest elements from the dataset defined by iterable
'''
import heapq
import itertools
from heapq import heappush, heappop


pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(heapq)
