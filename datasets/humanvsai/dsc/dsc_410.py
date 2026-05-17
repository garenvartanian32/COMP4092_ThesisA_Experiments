import hashlib

def check_sha1(filename, sha1_hash):
    with open(filename, 'rb') as f:
        file_hash = hashlib.sha1()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest() == sha1_hash