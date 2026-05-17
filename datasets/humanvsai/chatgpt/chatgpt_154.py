import subprocess

def clear_partition_table(block_device):
    subprocess.run(['sudo', 'sgdisk', '--zap-all', '--clear', block_device])
