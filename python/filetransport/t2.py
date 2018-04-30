#!/usr/bin/env python

"""
Start multipule thread to download url from website
"""

import os
import time


file_name = 'account_1/incoming/a1.txt'

os.chdir('/db/tmp/databank_fs')

dir_name = os.path.dirname(file_name)
print(dir_name)


if not os.path.isdir(dir_name):
    os.makedirs(dir_name)

with open(file_name,'w') as f:
    f.write('abd')

with open(file_name) as f:
    print(f.read())




def get_relative_file_name(full_path_file_name):
    """
    Return the relative file name based on the self.home_dir and full_path_file_name
    """
    home_dir = 'Databank/abcd'

    return full_path_file_name.replace(os.path.join(home_dir,''),'')


name = get_relative_file_name('Databank/abcd/incoming/a1.tsv')
print(name)