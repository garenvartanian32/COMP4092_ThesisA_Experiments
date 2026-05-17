import h5py

class Data:
    def __init__(self, data):
        self.data = data

    def write_to(self, group, append=False):
        if not append:
            # overwrite existing data
            for key in group.keys():
                del group[key]

        # write data to the group
        for i, item in enumerate(self.data):
            if append:
                key = 'item_' + str(len(group.keys()))
            else:
                key = 'item_' + str(i)
            group[key] = item