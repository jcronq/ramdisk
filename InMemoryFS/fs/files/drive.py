from fs.files.file import File
import fs.exceptions as exceptions

class Drive(File):
    def __init__(self):
        pass

    def size(self):
        exceptions.NOT_IMPLEMENTED('Drive.size')

    def clone(self):
        exceptions.NOT_IMPLEMENTED('Drive.clone')

