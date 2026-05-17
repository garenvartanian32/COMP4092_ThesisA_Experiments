def count_reads(file_name, paired_end):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        if paired_end:
            return len(lines) // 2
        else:
            return len(lines) // 4