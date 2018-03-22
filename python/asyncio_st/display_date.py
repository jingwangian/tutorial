#!/usr/bin/env python

"""
Example: Coroutine displaying the current date¶
"""

import asyncio
import datetime
import os

async def display_date(loop):
    end_time = loop.time() + 5.0
    print('PID = ',os.getpid())
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

print('PID = ',os.getpid())
loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()