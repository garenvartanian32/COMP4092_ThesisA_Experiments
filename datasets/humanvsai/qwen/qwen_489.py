def get_second_pass_opts_ebu(self):
    return '-filter:a loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json'

def get_second_pass_opts(self):
    """Return second pass loudnorm filter options string for ffmpeg"""
    return '-filter:a loudnorm=I=-16:TP=-1.5:LRA=11'

def get_first_pass_opts(self):
    """Return first pass loudnorm filter options string for ffmpeg"""
    return '-filter:a loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=-16:measured_TP=-1.5:measured_LRA=11:measured_thresh=-30:offset=0:linear=true:print_format=json'

def get_first_pass_opts_ebu(self):
    """Return first pass loudnorm filter options string for ffmpeg"""
    return '-filter:a loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=-16:measured_TP=-1.5:measured_LRA=11:measured_thresh=-30:offset=0:linear=true:print_format=json'

def get_first_pass_opts_custom(self, measured_I, measured_TP, measured_LRA, measured_thresh, offset, linear):
    """Return first pass loudnorm filter options string for ffmpeg with custom values"""
    return f'-filter:a loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={measured_I}:measured_TP={measured_TP}:measured_LRA={measured_LRA}:measured_thresh={measured_thresh}:offset={offset}:linear={linear}:print_format=json'

def get_second_pass_opts_custom(self, I, TP, LRA):
    """Return second pass loudnorm filter options string for ffmpeg with custom values"""
    return f'-filter:a loudnorm=I={I}:TP={TP}:LRA={LRA}'