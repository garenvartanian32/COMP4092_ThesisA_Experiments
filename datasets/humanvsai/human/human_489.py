def get_second_pass_opts_ebu(self):
        if not self.loudness_statistics['ebu']:
            raise FFmpegNormalizeError(
                "First pass not run, you must call parse_loudnorm_stats first"
            )
        input_i = float(self.loudness_statistics['ebu']["input_i"])
        if input_i > 0:
            logger.warn("Input file had measured input loudness greater than zero ({}), capping at 0".format("input_i"))
            self.loudness_statistics['ebu']['input_i'] = 0
        opts = {
            'i': self.media_file.ffmpeg_normalize.target_level,
            'lra': self.media_file.ffmpeg_normalize.loudness_range_target,
            'tp': self.media_file.ffmpeg_normalize.true_peak,
            'offset': self.media_file.ffmpeg_normalize.offset,
            'measured_i': float(self.loudness_statistics['ebu']['input_i']),
            'measured_lra': float(self.loudness_statistics['ebu']['input_lra']),
            'measured_tp': float(self.loudness_statistics['ebu']['input_tp']),
            'measured_thresh': float(self.loudness_statistics['ebu']['input_thresh']),
            'linear': 'true',
            'print_format': 'json'
        }
        if self.media_file.ffmpeg_normalize.dual_mono:
            opts['dual_mono'] = 'true'
        return 'loudnorm=' + dict_to_filter_opts(opts)