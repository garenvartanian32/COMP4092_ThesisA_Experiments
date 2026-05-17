def run_script(dist_spec, script_name):
    import importlib.util
    import sys
    import os
    dist = importlib.util.find_spec(dist_spec)
    if not dist:
        raise ValueError(f'Could not find distribution: {dist_spec}')
    script_path = os.path.join(dist.origin, script_name)
    if not os.path.exists(script_path):
        raise ValueError(f'Could not find script: {script_name} in distribution: {dist_spec}')
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[script_name] = module
    spec.loader.exec_module(module)
    if hasattr(module, 'main'):
        module.main()
    else:
        raise ValueError(f"Script {script_name} does not have a 'main' function")