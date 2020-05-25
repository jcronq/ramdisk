from datetime import datetime
import fs.node_type as node_types

class iNode:

    def __init__(self, _type, _parent, _file):
        self.set_parent(_parent)
        self._file = _file
        self._type = _type
        now = datetime.now()
        self._create_ts = now
        self._update_ts = now
        self._access_ts = now

    def get_type(self):
        return self._type

    def get_file(self):
        return self._file
    
    def set_parent(self, _parent):
        self._parent = _parent

    def get_parent(self):
        return self._parent

    def size(self):
        return self._file.size()
    
    def stat(self):
        return f'Type: {self._type}, created: {self._create_ts}, updated: {self._update_ts}, accessed: {self._access_ts}, size: {self.size()}'

    def destroy(self):
        self.set_parent(None)
