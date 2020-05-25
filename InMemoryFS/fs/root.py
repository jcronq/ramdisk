from fs.inode import iNode
import fs.node_type as node_type
from fs.files.directory import Directory

class Root:
    _instance = None

    @staticmethod
    def inode():
        if Root._instance == None:
            Root._instance = Root()
        return Root._instance._root
    
    def __init__(self):
        directory = Directory()
        self._root = iNode(node_type.DIRECTORY, None, directory)

    