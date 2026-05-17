class MyClass:
    def __init__(self):
        self.exec_area = None

    def set_exec_area(self, exec_area):
        """Sets the exec area value.
        The exec area is a pool of host memory used to store pages
        translated by the JIT (they contain the native code
        corresponding to MIPS code pages).

        :param exec_area: exec area value (integer)"""
        self.exec_area = exec_area