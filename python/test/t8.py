#!/usr/bin/env python3
import enum
import odin

class FileStatus(enum.Enum):
    """
    Valid file states
    """
    New = 'new'
    Ready = 'ready'
    Moving = 'moving'
    Completed = 'completed'
    Error = 'error'
    Cancelled = 'cancelled'

class EndPointFile:
    """
    Represent a file in the endpoint and hold the file status.
    """
    ST_NEW = FileStatus.New
    ST_READY = "ready"
    ST_MOVING = "moving"
    ST_MOVE_COMP = "completed"
    ST_MOVE_ERROR = "error"
    ST_MOVE_CANCELLED = "cancelled"

    def __init__(self, file_name, file_state = ST_NEW):
        self.file_name = file_name
        self.file_state = file_state

    def __repr__(self):
        return "{} : {}".format(self.file_name,self.file_state)


fs = FileStatus.New
fs2 = EndPointFile.ST_NEW


ep_file1 = EndPointFile('a1.txt')
ep_file2 = EndPointFile('a2.txt', EndPointFile.ST_MOVING)

print(ep_file1)
print(ep_file2)
print(fs)
print(fs2)
print(fs == fs2)


class Event(odin.Resource):
    """
    Base class for all events
    """
    class Meta:
        abstract = True
        namespace = 'au.com.databank.v4.event'

    def __repr__(self):
        return repr_format(self)


#################################################
# File Transport Events

class FileEvent(Event):
    class Meta:
        abstract = True

    transaction = odin.UUIDField(
        doc_text="Unique ID for the file instance."
    )
    file_ref = odin.StringField(
        doc_text="URI Style file reference."
    )
    size = odin.IntegerField(
        doc_text="Size of file (in bytes)."
    )

    def __repr__(self):
        return repr_format(self, 'transaction={transaction!r}; file_ref={file_ref!r}')


file_event1 = FileEvent(transaction="hello")

file_event2 = FileEvent(transaction="hello world")

print(file_event1.transaction)
print(file_event2.transaction)

print(id(file_event1))
print(id(file_event2))