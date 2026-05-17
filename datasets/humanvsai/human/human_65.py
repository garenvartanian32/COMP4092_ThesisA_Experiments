def process_directories(self):
        for i, (base_dir, target_dir, paths) in enumerate(zip(
                self.in_dir, self.out_dir, map(os.walk, self.in_dir))):
            self._in_dir_count = i
            self.recursive_processing(base_dir, target_dir, paths)