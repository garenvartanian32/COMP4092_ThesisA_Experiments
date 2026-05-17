def check_sha1(filename, sha1_hash):
    import hashlib
    with open(filename, 'rb') as f:
        file_content = f.read()
        calculated_hash = hashlib.sha1(file_content).hexdigest()
        return calculated_hash == sha1_hash