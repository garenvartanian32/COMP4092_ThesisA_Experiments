def zap_disk(block_device):
    import subprocess
    try:
        subprocess.run(['sgdisk', '--zap-all', block_device], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error clearing partition table on {block_device}: {e}')
    except FileNotFoundError:
        print("sgdisk command not found. Please install the 'gdisk' package.")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')