# Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
# This class should contain method serialize for serialize object to filename according to  type. 
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.

import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = 1
    BYTE = 2


class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'but with {exc_type.__name__} with name {exc_val}')

    def serialize(self, obj):
        if self.filetype == FileType.JSON:
            with open(self.filename, 'w') as f:
                json.dump(obj, f)
        elif self.filetype == FileType.BYTE:
            with open(self.filename, 'wb') as f:
                pickle.dump(obj, f)


def serialize(obj, filename, filetype):
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(obj)
