def get_sitej(structure, connectivity, site_index, image_index):
    sitej_index = connectivity.index((1, site_index, image_index))
    sitej = structure[connectivity[sitej_index][1]]
    return sitej
