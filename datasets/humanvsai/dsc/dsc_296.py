def generate_dependencies(obj):
    dependencies = {
        'dependencies': {
            'bar': ['foo'],
        },
    }

    for key, value in dependencies['dependencies'].items():
        if key in obj:
            for dep in value:
                if dep not in obj:
                    return False
    return True