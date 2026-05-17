def count_reads(self, file_name, paired_end):
        _, ext = os.path.splitext(file_name)
        if not (is_sam_or_bam(file_name) or is_fastq(file_name)):
            # TODO: make this an exception and force caller to handle that
            # rather than relying on knowledge of possibility of negative value.
            return -1
        if is_sam_or_bam(file_name):
            param_text = "-c" if ext == ".bam" else "-c -S"
            return self.samtools_view(file_name, param=param_text)
        else:
            num_lines = self.count_lines_zip(file_name) \
                    if is_gzipped_fastq(file_name) \
                    else self.count_lines(file_name)
            divisor = 2 if paired_end else 4
            return int(num_lines) / divisor