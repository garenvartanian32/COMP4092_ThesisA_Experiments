def combinate(values):
    return tuple(values)

def aggregate(values):
    """aggregate multiple values into a list"""
    return list(values)

def concatenate(values):
    """concatenate multiple strings into a single string"""
    return ''.join(values)

def combine(values):
    """combine multiple dictionaries into a single dictionary"""
    result = {}
    for value in values:
        result.update(value)
    return result

def merge(values):
    """merge multiple lists into a single list"""
    result = []
    for value in values:
        result.extend(value)
    return result

def join(values, separator=''):
    """join multiple strings with a separator"""
    return separator.join(values)

def flatten(values):
    """flatten a list of lists into a single list"""
    result = []
    for value in values:
        if isinstance(value, list):
            result.extend(flatten(value))
        else:
            result.append(value)
    return result

def split(values, delimiter):
    """split a string into a list of substrings"""
    return values.split(delimiter)

def reverse(values):
    """reverse the order of elements in a list or string"""
    return values[::-1]

def sort(values):
    """sort the elements in a list"""
    return sorted(values)

def unique(values):
    """return a list of unique elements from a list"""
    return list(set(values))

def count(values, element):
    """count the occurrences of an element in a list"""
    return values.count(element)

def filter_values(values, condition):
    """filter elements in a list based on a condition"""
    return [value for value in values if condition(value)]

def map_values(values, function):
    """apply a function to each element in a list"""
    return [function(value) for value in values]

def reduce_values(values, function, initializer=None):
    """reduce a list to a single value using a function"""
    from functools import reduce
    return reduce(function, values, initializer)

def zip_values(*iterables):
    """zip multiple iterables into a list of tuples"""
    return list(zip(*iterables))

def unzip_values(values):
    """unzip a list of tuples into multiple lists"""
    return list(zip(*values))

def transpose(matrix):
    """transpose a matrix (list of lists)"""
    return list(zip(*matrix))

def rotate(matrix):
    """rotate a matrix 90 degrees clockwise"""