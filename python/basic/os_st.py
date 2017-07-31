#!/usr/bin/env python3

'''
os study:

Methods:
CLD_CONTINUED,CLD_DUMPED,CLD_EXITED,CLD_TRAPPED,EX_CANTCREAT,EX_CONFIG,EX_DATAERR,EX_IOERR
EX_NOHOST,EX_NOINPUT,EX_NOPERM,EX_NOUSER,EX_OK,EX_OSERR,EX_OSFILE,EX_PROTOCOL
EX_SOFTWARE,EX_TEMPFAIL,EX_UNAVAILABLE,EX_USAGE,F_LOCK,F_OK,F_TEST,F_TLOCK
F_ULOCK,MutableMapping,NGROUPS_MAX,O_ACCMODE,O_APPEND,O_ASYNC,O_CLOEXEC,O_CREAT
O_DIRECT,O_DIRECTORY,O_DSYNC,O_EXCL,O_LARGEFILE,O_NDELAY,O_NOATIME,O_NOCTTY
O_NOFOLLOW,O_NONBLOCK,O_PATH,O_RDONLY,O_RDWR,O_RSYNC,O_SYNC,O_TRUNC
O_WRONLY,POSIX_FADV_DONTNEED,POSIX_FADV_NOREUSE,POSIX_FADV_NORMAL,POSIX_FADV_RANDOM,POSIX_FADV_SEQUENTIAL,POSIX_FADV_WILLNEED,PRIO_PGRP
PRIO_PROCESS,PRIO_USER,P_ALL,P_NOWAIT,P_NOWAITO,P_PGID,P_PID,P_WAIT
RTLD_DEEPBIND,RTLD_GLOBAL,RTLD_LAZY,RTLD_LOCAL,RTLD_NODELETE,RTLD_NOLOAD,RTLD_NOW,R_OK
SCHED_BATCH,SCHED_FIFO,SCHED_IDLE,SCHED_OTHER,SCHED_RESET_ON_FORK,SCHED_RR,SEEK_CUR,SEEK_DATA
SEEK_END,SEEK_HOLE,SEEK_SET,ST_APPEND,ST_MANDLOCK,ST_NOATIME,ST_NODEV,ST_NODIRATIME
ST_NOEXEC,ST_NOSUID,ST_RDONLY,ST_RELATIME,ST_SYNCHRONOUS,ST_WRITE,TMP_MAX,WCONTINUED
WCOREDUMP,WEXITED,WEXITSTATUS,WIFCONTINUED,WIFEXITED,WIFSIGNALED,WIFSTOPPED,WNOHANG
WNOWAIT,WSTOPPED,WSTOPSIG,WTERMSIG,WUNTRACED,W_OK,XATTR_CREATE,XATTR_REPLACE
XATTR_SIZE_MAX,X_OK,_Environ,
__all__,__builtins__,__cached__,__doc__,__file__
__loader__,__name__,__package__,__spec__,_execvpe,_exists,_exit,_fwalk
_get_exports_list,_putenv,_spawnvef,_unsetenv,_wrap_close,

abort,access,altsep
chdir,chmod,chown,chroot,close,closerange,confstr,confstr_names,
cpu_count,ctermid,curdir,
defpath,device_encoding,devnull,dup,dup2
environ,environb,errno,error,execl,execle,execlp,execlpe
execv,execve,execvp,execvpe,extsep,fchdir,fchmod,fchown
fdatasync,fdopen,fork,forkpty,fpathconf,fsdecode,fsencode,fstat
fstatvfs,fsync,ftruncate,fwalk,get_blocking,get_exec_path,get_inheritable,get_terminal_size
getcwd,getcwdb,getegid,getenv,getenvb,geteuid,getgid,getgrouplist
getgroups,getloadavg,getlogin,getpgid,getpgrp,getpid,getppid,getpriority
getresgid,getresuid,getsid,getuid,getxattr,initgroups,isatty,kill
killpg,lchown,linesep,link,listdir,listxattr,lockf,lseek
lstat,major,makedev,makedirs,minor,mkdir,mkfifo,mknod
name,nice,open,openpty,pardir,path,pathconf,pathconf_names
pathsep,pipe,pipe2,popen,posix_fadvise,posix_fallocate,pread,putenv
pwrite,read,readlink,readv,remove,removedirs,removexattr,rename
renames,replace,rmdir,scandir,sched_get_priority_max,sched_get_priority_min,sched_getaffinity,sched_getparam
sched_getscheduler,sched_param,sched_rr_get_interval,sched_setaffinity,sched_setparam,sched_setscheduler,sched_yield,sendfile
sep,set_blocking,set_inheritable,setegid,seteuid,setgid,setgroups,setpgid
setpgrp,setpriority,setregid,setresgid,setresuid,setreuid,setsid,setuid
setxattr,spawnl,spawnle,spawnlp,spawnlpe,spawnv,spawnve,spawnvp
spawnvpe,st,stat,stat_float_times,stat_result,statvfs,statvfs_result,strerror
supports_bytes_environ,supports_dir_fd,supports_effective_ids,supports_fd,supports_follow_symlinks,symlink,sync,sys
sysconf,sysconf_names,system,tcgetpgrp,tcsetpgrp,terminal_size,times,times_result
truncate,ttyname,umask,uname,uname_result,unlink,unsetenv,urandom
utime,wait,wait3,wait4,waitid,waitid_result,waitpid,walk
write,writev,

'''
import os
import datetime

print(os.getcwd(), os.getcwdb())
print(os.getenv('PATH'))
print(os.putenv('PATH', os.getenv('PATH') + ':/db'))
print(os.getenv('PATH'))
# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
# printkey(os)


for root, dirs, files in os.walk('/db/github/tutorial/python/basic'):
    for file in files:
        full_path_file = os.path.join(root, file)
        print(full_path_file, os.path.getsize(full_path_file), os.path.getctime(full_path_file), os.path.getatime(full_path_file))

        d1 = datetime.datetime.fromtimestamp(os.path.getctime(full_path_file))
        print(d1.isoformat())
