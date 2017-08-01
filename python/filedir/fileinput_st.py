#!/usr/bin/env python3

'''
fileinput study

Functions:

filename()
    Return the name of the file currently being read. Before the first line has been read, returns None.

fileno()
    Return the integer “file descriptor” for the current file. When no file is opened (before the first line and between files), returns -1.

lineno()
    Return the cumulative line number of the line that has just been read. Before the first line has been read, returns 0. After the last line of the last file has been read, returns the line number of that line.

filelineno()
    Return the line number in the current file. Before the first line has been read, returns 0. After the last line of the last file has been read, returns the line number of that line within the file.

isfirstline()
    Returns true if the line just read is the first line of its file, otherwise returns false.

isstdin()
    Returns true if the last line was read from sys.stdin, otherwise returns false.

nextfile()
    Close the current file so that the next iteration will read the first line from the next file (if any); lines not read from the file will not count towards the cumulative line count. The filename is not changed until after the first line of the next file has been read. Before the first line has been read, this function has no effect; it cannot be used to skip the first file. After the last line of the last file has been read, this function has no effect.

close()
    Close the sequence.

'''
import fileinput
import os

dir = '/db2/github/tutorial/python'
# files = os.listdir(dir)
# print(files)
file_list = []
for root, dirs, files in os.walk(dir):
    [file_list.append((os.path.join(root, file))) for file in files]

    if len(dirs) > 0:
        print(dirs)

[print(x) for x in file_list]

with fileinput.input(files=file_list) as f:
    for line in f:
        if line.strip().find('python3') > 0:
            print('{}: {} :{}'.format(f.filename(), line.strip(), f.filelineno()))

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(obj)
