import os
import uuid

DATABASE_FILE = '/tmp/database'


class FileSystemDatabase:
    @staticmethod
    def write(value):
        # https://stackoverflow.com/a/2333979
        filename = '/tmp/' + uuid.uuid4().hex
        f = open(filename, 'w')
        f.write(str(value))
        f.flush()
        os.fsync(f.fileno())
        f.close()
        os.rename(filename, DATABASE_FILE)

    @staticmethod
    def read():
        f = open(DATABASE_FILE)
        value = f.readline()
        f.close()
        return int(value)
