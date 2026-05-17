def run(self, executable: Executable,
            memory_map: Dict[str, List[Union[int, float]]] = None) -> np.ndarray:
        self.qam.load(executable)
        if memory_map:
            for region_name, values_list in memory_map.items():
                for offset, value in enumerate(values_list):
                    # TODO gh-658: have write_memory take a list rather than value + offset
                    self.qam.write_memory(region_name=region_name, offset=offset, value=value)
        return self.qam.run() \
            .wait() \
            .read_memory(region_name='ro')