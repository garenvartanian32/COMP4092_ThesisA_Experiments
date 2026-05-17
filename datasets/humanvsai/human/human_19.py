def get_metric_index(self, data_source):
        if data_source in self.index_dict:
            index = self.index_dict[data_source]
        else:
            index = self.class2index[self.ds2class[data_source]]
        return Index(index_name=index)