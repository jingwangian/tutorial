#!/usr/bin/env python


import os
import asyncio
import random
import time
import datetime
import signal


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

def ask_exit():
    print("Enter ask_exit")
    for task in asyncio.Task.all_tasks():
        task.cancel()

    asyncio.ensure_future(exit())  

# Stop the loop concurrently           
@asyncio.coroutine
def exit():                                              
    print("Enter exit function")
    loop = asyncio.get_event_loop()                      
    print("Stop")                                        
    loop.stop()
    print("Exit exit function")

def main():
    print("Enter main function")

    loop = asyncio.get_event_loop()
    loop.create_task(check_incoming_files())
    loop.create_task(check_file_status())

    for sig in (signal.SIGINT, signal.SIGTERM):          
        loop.add_signal_handler(sig, ask_exit) 

    try:
        print('before run_until_complete')
        loop.run_forever()
        # print('after run_forever')

        # loop.run_until_complete(start_tasks(loop))
        print('after run_until_complete')
    except KeyboardInterrupt:
        print("Recevied the KeyboardInterrupt")
        # ask_exit()
        loop.stop()
        loop.close()

    loop.close()
    print("Exit main function")    
if __name__ == '__main__':
    main()