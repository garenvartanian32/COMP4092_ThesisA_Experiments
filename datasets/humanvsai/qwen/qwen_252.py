def get_search_index(self, index):
    return self.client.get_search_index(index)

def create_search_index(self, index_name, schema):
    """Create a new Solr search index for Yokozuna.

        :param index_name: the name of the new yz index
        :type index_name: string
        :param schema: the schema definition for the new index
        :type schema: dict

        :rtype: bool"""
    return self.client.create_search_index(index_name, schema)