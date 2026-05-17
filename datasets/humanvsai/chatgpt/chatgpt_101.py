def find_child_characteristic(uuid):
    for child in parent_characteristic.getDescriptors():
        if child.uuid == uuid:
            return child
    return None