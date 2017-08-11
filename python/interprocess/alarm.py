#!/usr/bin/env python3

'''
signal alarm study

Signal     Value     Action   Comment
──────────────────────────────────────────────────────────────────────
SIGHUP        1       Term    Hangup detected on controlling terminal
                             or death of controlling process
SIGINT        2       Term    Interrupt from keyboard
SIGQUIT       3       Core    Quit from keyboard
SIGILL        4       Core    Illegal Instruction
SIGABRT       6       Core    Abort signal from abort(3)
SIGFPE        8       Core    Floating point exception
SIGKILL       9       Term    Kill signal
SIGSEGV      11       Core    Invalid memory reference
SIGPIPE      13       Term    Broken pipe: write to pipe with no
                             readers
SIGALRM      14       Term    Timer signal from alarm(2)
SIGTERM      15       Term    Termination signal
SIGUSR1   30,10,16    Term    User-defined signal 1
SIGUSR2   31,12,17    Term    User-defined signal 2
SIGCHLD   20,17,18    Ign     Child stopped or terminated
SIGCONT   19,18,25    Cont    Continue if stopped
SIGSTOP   17,19,23    Stop    Stop process
SIGTSTP   18,20,24    Stop    Stop typed at terminal
SIGTTIN   21,21,26    Stop    Terminal input for background process
SIGTTOU   22,22,27    Stop    Terminal output for background process

'''
import signal
import time
import os

count = 10


class MyException(Exception):
    def __init__(self, error=None):
        self.error = error

    def __str__(self):
        return self.error if self.error is not None else 'my_exception'
        # if error is None:
        #     return 'my_exception'


class TimeOut():
    class Timeout_Exception(Exception):
        def __init__(self, err="Timeout_Exception"):
            self.err = err

        def __str__(self):
            return self.err

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        print('Start to time')
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        # signal.alarm(0)
        print('Exist Timeout')
        # [print(type(x)) for x in args]

    def raise_timeout(self, *args):
        signal.alarm(0)  # Close the time out here
        print('Time out')
        [print(type(x)) for x in args]
        raise self.Timeout_Exception()


def sig_handle(signum, frame):
    global count
    if signum == signal.SIGQUIT:
        print("Receive SIGQUIT")
    elif signum == signal.SIGINT:
        print("Receive SIGINT")
        count = 0
    elif signum == signal.SIGTERM:
        print("Receive SIGTERM")
        raise MyException("Receive SIGTERM")
    elif signum == signal.SIGALRM:
        signal.alarm(0)
        raise MyException("It's time out")


def create_kill_script():
    with open('kill.sh', 'w') as f:
        f.write('echo "kill {}"\n'.format(os.getpid()))
        f.write('kill {}'.format(os.getpid()))


def main():
    global count
    print('Enter into main funtion with pid [{}]'.format(os.getpid()))
    create_kill_script()
    signal.signal(signal.SIGINT, sig_handle)
    signal.signal(signal.SIGTERM, sig_handle)
    signal.signal(signal.SIGQUIT, sig_handle)
    signal.signal(signal.SIGALRM, sig_handle)
    signal.alarm(5)
    try:
        # with TimeOut(5):
        while(1):
            time.sleep(1)
            print('count is {} now'.format(count))
            count -= 1
            if count <= 0:
                break

    except TimeOut.Timeout_Exception as e:
        print("go to main Timeout_Exception")
    except MyException as e:
        print(str(e))

    print('Exit main function')

if __name__ == '__main__':
    main()

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
