class MyClass:
    def __init__(self, lits=[], ubound=1, top_id=None):
        self.lits = lits
        self.ubound = ubound
        self.top_id = top_id

# Usage:
obj = MyClass(lits=[1, 2, 3], ubound=10, top_id='my_id')