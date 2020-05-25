from fs.files.file import File
import fs.exceptions as exceptions
from functools import reduce
from operator import add

class Directory(File):
    def __init__(self):
        self._children = {}

    def get_child(self, child_name):
        return self._children.get(child_name, None)
    
    def add(self, name, inode):
        self._children[name] = inode

    def remove(self, name):
        try:
            child = self._children.pop(name)
            child.destroy()
        except:
            raise exceptions.DIRECTORY_NOT_FOUND(f"cannot remove {name}: No such file or directory")

    def size(self):
        if len(self._children) <= 0:
            return 0
        
        children_sizes = [child.size() for child in self._children.items()]
        return reduce(add, children_sizes)

    def clone(self):
        directory_clone = Directory()
        if len(self._children) > 0:
            for name, child in self._children.items():
                directory_clone.add(name, child.clone())

        return directory_clone

    def ls(self):
        return " ".join(list(self._children.keys()))