from fs.inode import iNode
import fs.exceptions as exceptions
import fs.node_type as node_type
from fs.root import Root
from fs.files.directory import Directory
from fs.files.document import Document

def get_path(path_str):
    if path_str == '/':
        return []
    return path_str.split('/')[1:]

def get_inode(source_path):
    # Relative Paths are not suppported at this time
    current_inode = Root.inode()

    for path_part in source_path:
        current_inode = current_inode.get_file().get_child(path_part)

        if current_inode is None:
            return None

    return current_inode

def copy(source, target):
    source_path = get_path(source)
    target_path = get_path(target)

    source_inode = get_inode(source_path)
    source_file = source_inode.get_file(source_inode)
    source_type = source_inode.get_type()

    target_parent_inode = get_inode(target_path[:-1])
    target_fname = target_path[-1]

    new_file = source_file.clone()
    new_inode = iNode(source_type, target_parent_inode, new_file)
    
    target_directory = target_parent_inode.get_file()
    target_directory.add(target_fname, new_inode)

    return new_inode

def move(source, target):
    source_path = get_path(source)
    target_path = get_path(target)

    source_inode = get_inode(source_path)
    source_fname = source_path[-1]
    source_directory = source_inode.get_parent().get_file()

    target_parent_inode = get_inode(target_path[:-1])
    if target_parent_inode.get_type() is not node_type.DIRECTORY:
        raise exceptions.NOT_A_DIRECTORY('/' + '/'.join(target_path[:-1]))
    target_directory = target_parent_inode.get_file()
    target_fname = target_path[-1]

    source_directory.remove(source_fname)
    source_inode.set_parent(target_parent_inode)
    target_directory.add(target_fname, source_inode)

def mkdir(target):
    target_path = get_path(target)
    target_parent_inode = get_inode(target_path[:-1])

    directory_name = target_path[-1]
    new_directory = Directory()

    new_inode = iNode(node_type.DIRECTORY, target_parent_inode, new_directory)

    target_parent_inode.get_file().add(directory_name, new_inode)

def size(target):
    target_path = get_path(target)
    target_inode = get_inode(target_path)

    return target_inode.size()

def ls(target):
    target_path = get_path(target)
    target_inode = get_inode(target_path)

    target_type = target_inode.get_type()

    if target_type == node_type.DIRECTORY:
        return target_inode.get_file().ls()

def remove(target):
    pass

def touch(target):
    target_path = get_path(target)
    target_inode = get_inode(target_path)

    if target_inode is None:
        parent_inode = get_inode(target_path[:-1])
        if parent_inode.get_type() != node_type.DIRECTORY:
            raise exceptions.NOT_A_DIRECTORY(target_path[:-1])
        
        new_document = Document()
        new_inode = iNode(node_type.DOCUMENT, parent_inode, new_document)
        parent_inode.get_file().add(target_path[-1], new_inode)

    
def write(target, data, append = False):
    target_path = get_path(target)
    target_inode = get_inode(target_path)

    if target_inode is None:
        touch(target)
        target_inode = get_inode(target_path)

    if target_inode.get_type() != node_type.DOCUMENT:
        raise exceptions.NOT_A_DOCUMENT(target_inode.get_type())

    document = target_inode.get_file()
    document.write(data, append)

def read(target):
    target_path = get_path(target)
    target_inode = get_inode(target_path)

    if target_inode.get_type() != node_type.DOCUMENT:
        raise exceptions.NOT_A_DOCUMENT(target_inode.get_type())

    document = target_inode.get_file()
    return document.read()
