#!/usr/bin/env python3

import time
from paramiko.sftp_attr import SFTPAttributes


s1 = SFTPAttributes()
s1.st_size = 2044
s1.st_mode = 33277
s1.st_uid = 1000
s1.st_gid = 1000
s1.st_atime = 1526254738
s1.st_mtime = 1525084270
s1.filename = 'abcd01/incoming/a1.txt'
print(s1)


s1 = "st_mode=33277, st_uid=1000, st_gid=1000,st_size=645, st_atime=1526254738, st_mtime=1525084270, st_ctime=1525084270"


def get_sftp_attributes(filename, st_size=1024, st_mode=33277, st_uid=1000, st_gid=1000, st_atime=None, st_mtime=None):
    sftp_attr = SFTPAttributes()

    sftp_attr.filename = filename
    sftp_attr.st_size = st_size
    sftp_attr.st_mode = st_mode
    sftp_attr.st_uid = st_uid
    sftp_attr.st_gid = st_gid
    if not st_atime:
        st_atime = time.time()

    sftp_attr.st_atime = st_atime

    if not st_mtime:
        st_mtime = time.time()

    sftp_attr.st_mtime = st_mtime

    return sftp_attr


sftp_file_create_list = [
    ('abcd01/incoming/sftp_a1_100.tsv', 100),
    ('abcd01/incoming/sftp_a1_100k.tsv', 1024 * 100),
    ('abcd01/incoming/sftp_a1_1000k.tsv', 1024 * 1000),
    ('abcd01/incoming/sftp_a1_50mb.tsv', 1024 * 10240 * 5),
    ('abcd01/incoming/sftp_a1_100mb.tsv', 1024 * 102400),
    ('abcd02/incoming/sftp_a2_100k.tsv', 1024 * 100),
    ('abcd02/incoming/sftp_a2_50mb.tsv', 1024 * 10240 * 5),
]

a1 = get_sftp_attributes(*('abcd01/incoming/sftp_a1_100.tsv', 100))
print(a1)

[print(get_sftp_attributes(*x)) for x in sftp_file_create_list]
