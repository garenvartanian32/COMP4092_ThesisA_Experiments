import os

def _get_cropped_file_names(self):
    common_prefix = os.path.commonprefix(self.files)
    common_suffix = os.path.commonprefix([f[::-1] for f in self.files])[::-1]

    cropped_file_names = [f[len(common_prefix):-len(common_suffix)] if f.startswith(common_prefix) and f.endswith(common_suffix) else f for f in self.files]

    return cropped_file_names