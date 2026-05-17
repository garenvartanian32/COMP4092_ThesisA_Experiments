def has_material(self, new_material):
    return new_material in self.materials

def add_material(self, new_material):
    """Add a new material to the object's materials list."""
    if not self.has_material(new_material):
        self.materials.append(new_material)
    else:
        print(f"Material '{new_material}' already exists.")

def remove_material(self, material_to_remove):
    """Remove a material from the object's materials list."""
    if material_to_remove in self.materials:
        self.materials.remove(material_to_remove)
    else:
        print(f"Material '{material_to_remove}' not found.")

def list_materials(self):
    """List all materials in the object's materials list."""
    if self.materials:
        print('Materials:')
        for material in self.materials:
            print(f'- {material}')
    else:
        print('No materials available.')

class MaterialManager:

    def __init__(self):
        self.materials = []
manager = MaterialManager()