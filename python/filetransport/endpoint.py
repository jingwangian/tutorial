"""
EndPoint Definition
"""

import abc
from dtb.servers.smtp import connection

class SourceEndPoint(metaclass=abc.ABCMeta):
    """
    The ABC class for EndPoint as source entry
    """

    @abc.abstractmethod
    def open(self, filename, mode, bufsize):
        """
        Return a file-like object.

        The filename may include the relative path if necessary. 
        Example: filename='incoming/a1.tsv'
        """

    @abc.abstractmethod
    def stat(self, path):
        """
        Retrieve information about a file on the given path
        """

    @abc.abstractmethod
    def remove(self, path):
        """
        Remove the file at the given path.
        """

    @abc.abstractmethod
    def listdir(self, path, pattern):
        """
        Return a list containing names of the files which match the pattern.

        If no pattern is given then return all the files in the path.

        If the file is in the sub_path, then the relative path name will be as part of the file name 
        like 'incoming/a1.tsv'.

        Usage: 
            listdir(pattern = 'incoming/*.tsv')
            The return list is: ['incoming/a1.tsv','incoming/a2.tsv','incoming/a2.tsv' ]
        """


class DestEndPoint(metaclass=abc.ABCMeta):
    """
    The ABC class for EndPoint as destination entry
    """

    @abc.abstractmethod
    def transfer(src, dest, path, context):
        """
        Transfer a src file object to dest file object.

        """


class FSEndPoint(SourceEndPoint, DestEndPoint):
    """
    Hold a endpoint information
    """
    def __init__(self, name, type='fs'):
        self.name = name
        self.type = type
        self.sftp = None

    def __str__(self):
        return self.name

    def __call__(self, name=None):
        return(("here---"+name))
        # print("here---",name)

    def open(self, filename, mode='r', bufsize=-1):
        print("{} is opened".format(filename))

    def stat(self, path):
        print("The stat function is invoked")

    def remove(self, path):
        print("{} is removed".format(path))

    def listdir(self, path='.', pattern=None):
        print("In the listdir function")

    def transfer(self, src, dest, path, context):
        print("{} ---> {}".format(src,dest))



class SMTPEndPoint(DestEndPoint):
    """
    Hold a smtp endpoint information
    """
    def transfer(self, src, dest, path, context):
        print("SMTPEndPoint : {} ---> {}".format(src,dest))


class SFTPEndPoint(SourceEndPoint, DestEndPoint):
    """
    Hold a sftp endpoint information
    """
    def open(self, filename, mode='r', bufsize=-1):
        print("SFTPEndPoint: {} is opened".format(filename))

    def stat(self, path):
        print("SFTPEndPoint: The stat function is invoked")

    def remove(self, path):
        print("SFTPEndPoint: {} is removed".format(path))

    def listdir(self, path='.', pattern=None):
        print("SFTPEndPoint: In the listdir function")

    def transfer(self, src, dest, path, context):
        print("SFTPEndPoint: {} ---> {}".format(src,dest))


class EndPointFactory:
    """
    Create a endpoint instance
    """

    def __init__(self, config_name):
        self.config_name

    def __call__(self)
        endpoint = []
        return endpoint