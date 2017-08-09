#!/usr/bin/env python3

'''
signal study

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


def sig_handle(signum, frame):
    global count
    if signum == signal.SIGQUIT:
        print("Receive SIGQUIT")
    elif signum == signal.SIGINT:
        print("Receive SIGINT")
        count = 0
    elif signum == signal.SIGTERM:
        print("Receive SIGTERM")


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
    while(1):
        time.sleep(1)
        count -= 1
        if count <= 0:
            break

    print('Exit main function')

if __name__ == '__main__':
    main()

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(threading)
