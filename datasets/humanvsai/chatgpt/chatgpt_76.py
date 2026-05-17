def has_material(material_name):
    """
    Takes in a material name and checks if it already exists.
    Returns True if the material exists, False if it does not.
    """
    # Assume we have a list of existing materials called 'existing_materials'
    existing_materials = ["wood", "steel", "plastic", "glass"]
    
    if material_name in existing_materials:
        return True
    else:
        return False
