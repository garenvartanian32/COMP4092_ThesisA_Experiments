from collections import defaultdict

class Traversal:
    def group(self, itr, key_func):
        group_dict = defaultdict(list)
        for item in itr:
            key = key_func(item)
            group_dict[key].append(item)
        return group_dict

class Flow:
    def __init__(self, iterable):
        self.iterable = iterable
        
    def __getitem__(self, name):
        return getattr(self, name)
    
    def group(self, key_func):
        traversal = Traversal()
        return traversal.group(self.iterable, key_func)
    
    def unbox(self):
        return self.iterable
