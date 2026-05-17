def MetatagDistinctValuesGet(metatag_name, namespace):
    # assume metatags variable is a list of metatags containing name and namespace keys
    distinct_values = set([tag[metatag_name] for tag in metatags if tag['namespace'] == namespace])
    return True
