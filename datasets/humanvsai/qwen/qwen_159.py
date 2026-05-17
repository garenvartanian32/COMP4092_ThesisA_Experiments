def count_reads(self, file_name, paired_end):
    with open(file_name, 'r') as file:
        line_count = sum((1 for line in file))
        if paired_end:
            read_count = line_count // 2
        else:
            read_count = line_count // 4
        return read_count