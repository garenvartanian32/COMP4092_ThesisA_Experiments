import hashlib
import os

def get_checksum_and_size(file_path, hash_constructor):
    hash_obj = hashlib.new(hash_constructor)
    file_size = 0

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_obj.update(chunk)
            file_size += len(chunk)

    checksum = hash_obj.hexdigest()
    return checksum, file_size
