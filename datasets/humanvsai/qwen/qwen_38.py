def set_exec_area(self, exec_area):
    self.exec_area = exec_area

def get_exec_area(self):
    """Gets the exec area value.
        The exec area is a pool of host memory used to store pages
        translated by the JIT (they contain the native code
        corresponding to MIPS code pages).

        :return: exec area value (integer)"""
    return self.exec_area

def set_exec_area_size(self, exec_area_size):
    """Sets the exec area size value.
        The exec area size is the size of the pool of host memory
        allocated for the exec area.

        :param exec_area_size: exec area size value (integer)"""
    self.exec_area_size = exec_area_size

def get_exec_area_size(self):
    """Gets the exec area size value.
        The exec area size is the size of the pool of host memory
        allocated for the exec area.

        :return: exec area size value (integer)"""
    self.exec_area_size = exec_area_size
    return self.exec_area_size