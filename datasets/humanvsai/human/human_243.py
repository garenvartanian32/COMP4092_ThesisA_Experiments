def MetatagDistinctValuesGet(self, metatag_name, namespace = None):
        ns = "default" if namespace is None else namespace
        if self.__SenseApiCall__("/metatag_name/{0}/distinct_values.json", "GET", parameters = {'namespace': ns}):
            return True
        else:
            self.__error__ = "api call unsuccessful"
            return False