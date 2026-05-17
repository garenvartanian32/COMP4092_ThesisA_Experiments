import os

def get_region_files():
    region_files = []
    for root, dirs, files in os.walk("/path/to/region/files"):
        for file in files:
            if file.endswith(".region"):
                region_files.append(os.path.join(root, file))
    return region_files
