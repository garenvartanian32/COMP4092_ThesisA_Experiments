def generate_dependencies(self):
    dependencies = {}
    for (prop, dep) in self.properties.items():
        if isinstance(dep, dict) and 'dependencies' in dep:
            dependencies[prop] = dep['dependencies']
    return dependencies