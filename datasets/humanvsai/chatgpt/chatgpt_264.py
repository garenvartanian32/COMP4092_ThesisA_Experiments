from collections import namedtuple

NNData = namedtuple('NNData', ['near_neighbor_sites', 'CN_dict', 'NN_sites_dict'])

def compute_near_neighbor(structure, n, length=None):
    near_neighbor_sites = []
    CN_dict = {}
    NN_sites_dict = {}
    return NNData(near_neighbor_sites, CN_dict, NN_sites_dict)