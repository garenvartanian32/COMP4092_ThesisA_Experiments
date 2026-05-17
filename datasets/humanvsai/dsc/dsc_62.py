import importlib
import subprocess

def run_script(dist_spec, script_name):
    """Locate distribution `dist_spec` and run its `script_name` script"""
    try:
        # Import the distribution
        dist = importlib.import_module(dist_spec)
    except ImportError:
        print(f"Could not import distribution {dist_spec}")
        return

    # Get the path to the script
    script_path = getattr(dist, script_name, None)

    if script_path is None:
        print(f"Could not find script {script_name} in distribution {dist_spec}")
        return

    # Run the script
    subprocess.run(["python", script_path])