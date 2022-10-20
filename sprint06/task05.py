# Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
# This class should contain method serialize for serialize object to filename according to  type. 
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.

import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = {'mode': 'w', 'dump': json.dump}
    BYTE = {'mode': 'wb', 'dump': pickle.dump}


class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype.value
        self._file = None

    def __enter__(self):
        self._file = open(self.filename, self.filetype['mode'])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def serialize(self, obj):
        self.filetype['dump'](obj, self._file)


def serialize(obj, filename, filetype):
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(obj)
