#!/usr/bin/env python3

'''
sys study
'''
import os
import sys

# my broken solution:
so = se = open("a.log", 'w', 0)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

os.dup2(sys.stdout.fileno(), so.fileno())
os.dup2(sys.stderr.fileno(), se.fileno())
###

print "kljhf sdf"

os.spawnve("P_WAIT", "/bin/ls", ["/bin/ls"], {})
os.execve("/bin/ls", ["/bin/ls"], os.environ)
