def get_previous_iter(iter):
    if iter.get_previous_sibling() is not None:
        return iter.get_previous_sibling()
    else:
        parent_iter = iter.get_parent()
        if parent_iter is not None:
            return parent_iter
        else:
            return None
