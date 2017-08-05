#!/usr/bin/env python3

# file_name = '/media/sf_hostshare/code.txt'

# dest_file_name = '/media/sf_hostshare/code_dest.txt'

# code_lines = []
# with open(file_name) as rf:
#     for line in rf:
#         if len(line.strip()) > 0:
#             code_lines.append(line)

# with open(dest_file_name, 'w') as wf:
#     [wf.write(x.lstrip()) for x in code_lines]

import subprocess
import shlex
from subprocess import Popen, PIPE

df_cmd_list = ['ssh,wangj@ub{},df,-h'.format(x) for x in range(1, 11)]


for df_cmd in df_cmd_list:
    print(df_cmd)
    dfcmd = df_cmd.split(',')
    print(dfcmd)
    ret = subprocess.run(dfcmd, stdout=subprocess.PIPE)
    [print(ret) for ret in filter(lambda x: x.find('/dev/xvda1') != -1, ret.stdout.decode().splitlines())]
    # [print(x) for x in ret.stdout.decode().splitlines()]
    # break
