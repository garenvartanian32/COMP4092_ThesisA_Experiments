def find_resource(file_path):
    try:
        file_object = open(file_path, 'r')
        return file_object
    except FileNotFoundError:
        raise IOError(f"File {file_path} not found")
    except Exception as e:
        raise IOError(f"Error opening file {file_path}: {str(e)}")
