def validate_dependencies(obj):
    if not isinstance(obj, dict):
        return False
    
    dependencies = {
        'bar': ['foo'],
    }
    
    foo_exists = 'foo' in obj
    
    if not foo_exists:
        if 'bar' in obj:
            return False
        return True
    
    for key in dependencies:
        if key in obj:
            for required_key in dependencies[key]:
                if required_key not in obj:
                    return False
            
    return True
