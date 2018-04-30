import os
import asyncio
import random
import time
import datetime


@asyncio.coroutine
def random_sleep(counter):
    delay = random.random()*5+3
    print("{} sleeps for {:.2f} seconds at {}".format(counter,delay,datetime.datetime.now()))
    time.sleep(2)
    yield from asyncio.sleep(delay)
    print("{} awakens at {}".format(counter, datetime.datetime.now()))

@asyncio.coroutine
def five_sleepers():
    print("Creating five tasks")

    tasks = [asyncio.async(random_sleep(i)) for i in range(5)]

    print("Sleeping after starting five tasks at {}".format(datetime.datetime.now()))
    # time.sleep(3)
    yield from asyncio.sleep(5)
    print("Waking and waiting for five tasks at {}".format(datetime.datetime.now()))
    yield from asyncio.wait(tasks)

    print("Exit from five_sleepers")

asyncio.get_event_loop().run_until_complete(five_sleepers())
