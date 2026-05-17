import subprocess

def close_process(proc):
    proc.terminate()
    proc.wait()
