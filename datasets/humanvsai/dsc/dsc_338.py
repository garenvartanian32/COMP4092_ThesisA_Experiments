import os
import collections

def count_characters(root):
    out = collections.defaultdict(int)
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            with open(os.path.join(dirpath, filename), 'r') as f:
                for char in f.read():
                    out[char] += 1
    return out