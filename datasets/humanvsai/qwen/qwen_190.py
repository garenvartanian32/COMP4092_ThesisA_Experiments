def _get_cropped_file_names(self):
    common_prefix = os.path.commonprefix(self.files)
    common_suffix = os.path.commonprefix([os.path.splitext(f)[0] for f in self.files])
    cropped_files = [f[len(common_prefix):] for f in self.files]
    cropped_files = [f[:-len(common_suffix)] for f in cropped_files]
    return cropped_files