def length(time_flags):
        # type: (int) -> int
        tf_each_size = 7
        if time_flags & (1 << 7):
            tf_each_size = 17
        time_flags &= 0x7f
        tf_num = 0
        while time_flags:
            time_flags &= time_flags - 1
            tf_num += 1
        return 5 + tf_each_size * tf_num