#!/usr/bin/env python3
"""
This is an example that loop call for a while
"""

import asyncio
import datetime


def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 2.0) < end_time:
        print("Before call_later")
        loop.call_later(1, display_date, end_time, loop)
        print("After call_later")
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
print("Before call_soon")
loop.call_soon(display_date, end_time, loop)
print("After call_soon")

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
