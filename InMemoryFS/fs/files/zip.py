from fs.files.file import File
import fs.exceptions as exceptions

class Zip(File):
    
    def __init__(self):
        pass
    
    def size(self):
        raise exceptions.NOT_IMPLEMENTED("Zip.size")

    def clone(self):
        raise exceptions.NOT_IMPLEMENTED("Zip.clone")

    