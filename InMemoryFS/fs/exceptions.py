class DIRECTORY_NOT_FOUND(Exception):
    def __init__(self, error = "No such file or directory"):
        print(error)
        self.error = error

class NOT_A_DOCUMENT(Exception):
    def __init__(self, type_found):
        error = f"Error: Attempted to write to a '{type_found}'.  Only Documents can be written to."
        print(error)
        self.error = error

class NOT_A_DIRECTORY(Exception):
    def __init__(self, path):
        error = f"Error: '{path}' is not a directory."
        print(error)
        self.error = error

class NOT_IMPLEMENTED(Exception):
    def __init__(self, func_name):
        error = f'{func_name} Not Implemented.'
        print(error)
        self.error = error