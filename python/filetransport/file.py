#!/usr/bin/env python

"""
EndPoint Definition
"""

import datetime
import endpoint

class FileStatus:
    ST_NEW = 1
    ST_UPLOADED = 2
    ST_MOVING = 3
    ST_MOVED = 4
    ST_MOVING_FAILED = 4

    def __init__(self, pathname,size, src_point, dest_point):
        self.id = UUID() #Transaction ID
        self.pathname = pathname
        self.size = size
        self.timestamp = datetime.datetime.timestamp()
        self.src_point = ''  #Src endpoint name
        self.dest_point = '' #Dest endpoint name
        self.state = FileStatus.ST_NEW
        self.retry_times = 0


    def update(self, size, timestamp, src_point, dest_point):
        if size != self.size:
            self.timestamp = datetime.datetime.timestamp()
            self.size = size

        self.src_point = src_point
        self.dest_point = dest_point

class Files:
    def __init__(self):
        self.file_dict = {}
        self.etcd_client = None


    def update(self, filename, size, timestamp, src_point, dest_point):
        """
        Updated the file status
        """
        try:
            filestatus = self.file_dict["filename"]
        except KeyError:
            filestatus = FileStatus()
            self.etcd_client.write("/events", json.dumps(ev_value), append=True, ttl=3600*240).key

        fielstatus.update(size, timestamp, src_point, dest_point)

    def update_etcd(self, filename):
        """
        Update the 
        """

def get_file_list_from_ETCD():
    """
    """

def get_file_list(*args):
    file_list = []

    return file_list