def _included_frames(frame_list, frame_format):
    return INCLUDED_FRAMES.format(Nframes=len(frame_list),
                                  frame_dir=os.path.dirname(frame_list[0]),
                                  frame_format=frame_format)