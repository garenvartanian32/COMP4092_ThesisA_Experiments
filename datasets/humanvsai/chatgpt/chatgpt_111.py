def conduct_inventory(antenna_location, search_radius):
    """Conduct inventory of the area around the antennas."""
    inventory = []
    # Perform inventory within the search radius around the antenna location
    # and add the items found to the inventory list
    for item in search_area(antenna_location, search_radius):
        inventory.append(item)
    return inventory

def search_area(location, radius):
    """Return items found within the specified search radius."""
    # Here you would implement your search algorithm based on your specific use case.
    # This could include querying a database or scanning for nearby devices. 
    # For the sake of this example, we will simply return a hardcoded list of items.
    items_found = ["Item 1", "Item 2", "Item 3"]
    return items_found
