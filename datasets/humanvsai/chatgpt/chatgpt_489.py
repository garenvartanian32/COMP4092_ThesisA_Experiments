def get_ffmpeg_loudnorm_options(loudness_i=-24.0, true_peak=-2.0, offset=0.0, dual_mono=False):
    filters = []
    filters.append(f"loudnorm=i={loudness_i}:tp={true_peak}:offset={offset}")

    if dual_mono:
        filters.append("loudnorm=dual_mono=true")

    return ':'.join(filters)
