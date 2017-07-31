#!/usr/bin/env python3

'''
os.path study:

Methods:
__all__,__builtins__,__cached__,__doc__,__file__,__loader__,__name__,__package__
__spec__,_get_sep,_joinrealpath,_varprog,_varprogb,
abspath,altsep,basename
commonpath,commonprefix,curdir,defpath,devnull,dirname,exists,expanduser
expandvars,extsep,genericpath,getatime,getctime,getmtime,getsize,isabs
isdir,isfile,islink,ismount,join,lexists,normcase,normpath
os,pardir,pathsep,realpath,relpath,samefile,sameopenfile,samestat
sep,split,splitdrive,splitext,stat,supports_unicode_filenames,sys,
'''

import os.path


def printkey(obj):
    def f(n):
        return ',' if n % 8 > 0 else None
    [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
printkey(os.path)
