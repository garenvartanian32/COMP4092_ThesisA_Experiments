def convert_csv(str_val):
    if "OP_CSV" in str_val:
        # Guess an appropriate sequence
        sequence = 12345
        return sequence
    else:
        # Disable RBF but leave lock_time on
        sequence = 0xFFFFFFFD
        if "OP_CSV" not in str_val:
            return -1  # Fails if there's no constant before OP_CSV
        return sequence
