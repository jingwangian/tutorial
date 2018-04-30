#!/usr/bin/env python3


file_name = 't3.p'

def t1():
    f = None
    try:
        f = open(file_name)
        print(f.readline())
    # except FileNotFoundError:
    #     print("FileNotFoundError")
    #     print("return here")
    #     return 100
    finally:
        print("t1: Go to finally")
        if f:
            print("Close ",file_name)
            f.close()

    print("before return 10")

    return 10

def main():
    try:
        print("t1 = ",t1())
    except FileNotFoundError:
        print("main: FileNotFoundError")
        raise
    finally:
        print("main: Go to finally")

if __name__ == '__main__':
    main()