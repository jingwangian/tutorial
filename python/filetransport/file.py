#!/usr/bin/env python

"""
EndPoint Definition
"""

import datetime

MAX_UNCHANGED_TIME = 120s

class File:
    ST_NEW = 1
    ST_UPLOADED = 2
    ST_MOVING = 3
    ST_MOVED = 4
    ST_MOVING_FAILED = 4

    def __init__(self, pathname, size, src_point_name, dest_point_name):
        self.id = UUID() #Transaction ID
        self.pathname = pathname
        self.size = size
        self.timestamp = datetime.datetime.timestamp()
        self.src_point_name = ''  #Src endpoint name
        self.dest_point_name = '' #Dest endpoint name
        self.state = FileStatus.ST_NEW
        self.retry_times = 0
        self.rules = None
        self._state = self.ST_NEW

        self.state = self.ST_UPLOADING

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        """
        Switch the state 
        """
        self.report(value)
        self._state = value

    def report(self, value):
        """
        Report the event to the etcd and SQS
        """
        pass

    def update(self, size, timestamp, src_point, dest_point):
        if size != self.size:
            self.timestamp = datetime.datetime.timestamp()
            self.size = size

        self.src_point = src_point
        self.dest_point = dest_point

    def move(self):
        """
        Move the file from src_endpoint to dest_endpoint
        """
        src_endpoint = self.rules.get_src_endpoint(self.src_point_name)
        dest_endpoint = self.rules.get_src_endpoint(self.dest_point_name)

        src_file = src_endpoint.open()
        dest_file = dest_endpoint.open()

        context = None
        self.state = self.ST_MOVING

        # Here will put the task into a queue, will change it later
        dest_endpoint.transfer(src_file,dest_file,self.file_name, context)

    def has_uploaded(self):
        """
        Check the file has been uploaded.

        The main policy is to check how long the timestamp is unchanged. If it reach the MAX_UNCHANGED_TIME then it
        will be consindered to be unploaded finished.

        Return : True or False
        """
        return True

    def check_status(self):
        """
        Check the file status and make an action on it if state will be changed.
        """
        if self.state ==  self.ST_UPLOADING:
            if datetime.datetime.timestamp - self.timestamp > MAX_UNCHANGED_TIME:
                self.state = self.self.ST_UPLOADED
                self.move()
        elif self.state ==  self.ST_MOVING:


class Files:
    def __init__(self):
        self.file_dict = {}
        self.etcd_client = None


    def update(self, full_path_file_name, file_name, size, src_point_name, dest_point_name):
        """
        Updated the file status
        """
        try:
            file = self.file_dict["full_path_file_name"]
        except KeyError:
            file = File(file_name, size, src_point, dest_point)
            self.file_dict[full_path_file_name] = file

        fielstatus.update(size, timestamp, src_point, dest_point)

    def update_file_list_in_etcd(self, filename):
        """
        Added a new file into the filelist saved in ETCD
        """
        pass


class FilesFactory:
    """
    Create and return a files instance
    """
    def __init__(self, config_name):
        self.config_name

    def __call__(self)
        files = []
        return files