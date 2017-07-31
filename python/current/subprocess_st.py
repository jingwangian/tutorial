#!/usr/bin/env python3

'''
subprocess

CalledProcessError,CompletedProcess,DEVNULL,PIPE,Popen,STDOUT,SubprocessError,TimeoutExpired
_PIPE_BUF,_PLATFORM_DEFAULT_CLOSE_FDS,_PopenSelector,__all__,__builtins__,__cached__,__doc__,__file__
__loader__,__name__,__package__,__spec__,_active,_args_from_interpreter_flags,_cleanup,_mswindows
_posixsubprocess,_time,
builtins,call,check_call,check_output,errno,getoutput
getstatusoutput,io,list2cmdline,os,run,select,selectors,signal
sys,threading,time,warnings,

run() :  Return CompletedProcess

CompletedProcess class:
args, returncode,stdout,stderr


Method: Popen
'''

import shlex
import subprocess
import datetime
from subprocess import Popen, PIPE

ret = subprocess.run(['ls', '-l', '/db/github'], stdout=subprocess.PIPE)
l1 = ret.stdout
l1 = l1.decode().splitlines()
print(type(l1))

l2 = []
for x in l1:
    t = x.split()[5:8]
    date_string = ' '.join(t)
    # print(date_string)
#     try:
#         d1 = datetime.datetime.strptime(date_string, "%b %d %Y")
#         print(d1)
#         l2.append(d1)
#     except Exception as e:
#         pass
#         # print(e)
#     # if len(t) > 0:
#     #     l2.append(tuple(t))
#     #     d1 = datetime.strftime('')

# print(sorted(l2))
# l2=[tuple(x.split()[5:8]) for x in l1]

# print(sorted(l2))

# print(sorted(l2))

# for line in l1:
#     item_list = line.split()
#     print(item_list[5:8])


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
# printkey(subprocess)

# args = shlex.split('ls -l /db/github')
# print(args)
# p = subprocess.Popen(args)
# print(p)

with Popen(["ifconfig"], stdout=PIPE) as proc:
    [print(x) for x in proc.stdout.read().decode().splitlines()]
