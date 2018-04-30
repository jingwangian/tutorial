#!/usr/bin/env python


import os
import asyncio
import random
import time
import datetime


@asyncio.coroutine
def check_incoming_files():
    print("Enter the check_incoming_files")

    while True:
        delay = random.random()*5+2
        delay = 1
        print("+++ Running check_incoming_files will take {} seconds at {}".format(delay,datetime.datetime.now()))
        time.sleep(delay)

        print("+++ check_incoming_files : Sleep 5 senconds")        
        yield from asyncio.sleep(5)
        print("+++ check_incoming_files awakens at {}".format(datetime.datetime.now()))

    print("Exit the check_incoming_files")

@asyncio.coroutine
def check_file_status():
    print("Enter check_file_status")
    while True:
        delay = random.random()*5+2
        delay = 1
        print("*** Running check_file_status will take {} seconds at {}".format(delay,datetime.datetime.now()))
        time.sleep(delay)

        print("*** check_file_status : Sleep 5 senconds")        
        yield from asyncio.sleep(8)
        print("*** check_file_status awakens at {}".format(datetime.datetime.now()))

    print("Exit check_file_status")

@asyncio.coroutine
def start_tasks(loop):
    print("Enter start_tasks")

    tasks = []

    tasks.append(asyncio.ensure_future(check_incoming_files()))
    tasks.append(asyncio.ensure_future(check_file_status()))

   
    print("Sleeping after starting tasks at {}".format(datetime.datetime.now()))
    yield from asyncio.sleep(5)
    print("Waking and waiting for tasks at {}".format(datetime.datetime.now()))
    yield from asyncio.wait(tasks)


    print("Exit from start_tasks")


def main():
    print("Enter main function")

    loop = asyncio.get_event_loop()
    try:
        print('before run_until_complete')
        # loop.run_forever()
        # print('after run_forever')
        loop.run_until_complete(start_tasks(loop))
        print('after run_until_complete')
    except KeyboardInterrupt:
        print("Recevied the KeyboardInterrupt")
        loop.stop()
        loop.close()

    print("Exit main function")    
if __name__ == '__main__':
    main()