import subprocess

def zap_disk(block_device):
    """Clear a block device of partition table. Relies on sgdisk, which is
    installed as part of the 'gdisk' package in Ubuntu.

    :param block_device: str: Full path of block device to clean.
    """
    try:
        # Run the sgdisk command to zap the disk
        subprocess.run(['sgdisk', '--zap-all', block_device], check=True)
        print(f"Successfully zapped {block_device}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to zap {block_device}. Error: {str(e)}")

# Example usage:
zap_disk('/dev/sdb')