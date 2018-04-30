#!/usr/bin/env python3
import concurrent.futures
import time
from concurrent.futures import ProcessPoolExecutor

def fun1(sleep_num):
    print("Enter fun1 with sleep number = {}".format(sleep_num))
    print("sleep {} seconds".format(sleep_num))
    time.sleep(sleep_num)
    print("Leave fun1 with sleep number = {}".format(sleep_num))

    return sleep_num*10


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        print("Enter main function")
        future_list = []
        for n in range(5,30,5):
            future = executor.submit(fun1, n)
            future_list.append((n,future))

        time.sleep(7)

        while True:
            try:
                for n,f in future_list:
                    if f.running():
                        print("{} is running".format(n))
                    elif f.done():
                        print("{} is done".format(n))
                        print("result = {} for {}".format(f.result(),n))

                time.sleep(6)

            except KeyboardInterrupt:
                print("Exit main function")
                break

                
    
if __name__ == '__main__':
    main()