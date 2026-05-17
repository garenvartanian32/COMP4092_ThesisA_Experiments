import math

def getEntropies(m):
    """Recursively get the current and max entropies from every child module

    :param m: any module

    :return: (currentEntropy, maxEntropy)
    """
    # Assuming m is a list of child modules
    if not m:
        return 0, 0

    currentEntropy = sum([-p * math.log2(p) for p in m])
    maxEntropy = math.log2(len(m))

    return currentEntropy, maxEntropy