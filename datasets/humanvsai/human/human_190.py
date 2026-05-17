def _get_cropped_file_names(self):
        files = [ff.name for ff in self.files]
        prefix = commonprefix(files)
        suffix = commonprefix([f[::-1] for f in files])[::-1]
        cropped = [f[len(prefix):-len(suffix)] for f in files]
        return cropped