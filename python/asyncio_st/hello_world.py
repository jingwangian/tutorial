#!/usr/bin/env python

import asyncio
import os
import time

def hello_world(loop):
    print('Hello World')
    print('PID = ',os.getpid())
    time.sleep(2)
    # loop.stop()

def hello_world_2(loop):
    print('Hello World2')
    print('PID = ',os.getpid())
    time.sleep(2)
    loop.stop()  #comment this will let the run_forever run always!!!

loop = asyncio.get_event_loop()

print('PID = ',os.getpid())
# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)
loop.call_soon(hello_world_2, loop)

# Blocking call interrupted by loop.stop()
print('before run_forever')
loop.run_forever()
print('after run_forever')
loop.close()