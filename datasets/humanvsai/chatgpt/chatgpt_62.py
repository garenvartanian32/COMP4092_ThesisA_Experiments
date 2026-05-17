import os
import sys
import subprocess

def run_script_from_dist(dist_spec, script_name):
    _, dist = next(filter(lambda d: d[0] == dist_spec, sys.path_importer_cache.items()), (None, None))
    if dist is not None:
        script_path = os.path.join(dist.path, script_name)
        if os.path.exists(script_path):
            subprocess.run(f"python {script_path}")
        else:
            print(f"Error: script {script_name} not found in distribution {dist_spec}")
    else:
        print(f"Error: distribution {dist_spec} not found")
