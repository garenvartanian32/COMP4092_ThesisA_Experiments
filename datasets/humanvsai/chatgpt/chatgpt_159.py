def count_reads(file_name: str, paired_end: bool) -> int:
    if paired_end:
        with open(file_name, 'r') as f1, open(file_name.replace('R1', 'R2'), 'r') as f2:
            return sum(1 for _ in f1)/2 + sum(1 for _ in f2)/2
    else:
        with open(file_name, 'r') as f:
            return sum(1 for _ in f)
