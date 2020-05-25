from fs.files.file import File

class Document(File):

    def __init__(self):
        self._data = ""
        
    def size(self):
        return len(self._data)

    def clone(self):
        document_clone = Document()
        document_clone.write(self._data)

    def write(self, data, append = False):
        if append:
            self._data = self._data + data
        else: 
            self._data = data
        
    def read(self, seek = 0, size = -1):
        if size < 0:
            size = len(self._data)
        return self._data[seek:seek+size]
