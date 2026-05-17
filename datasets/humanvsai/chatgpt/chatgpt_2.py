class Slice:
    @staticmethod
    def parse(v):
        slices = []
        for x in v.split(","):
            limits = x.split(":")
            start, end = None, None
            if len(limits) == 1:
                start = int(limits[0])
                end = start + 1
            elif len(limits) == 2:
                if limits[0] == '':
                    end = int(limits[1])
                elif limits[1] == '':
                    start = int(limits[0])
                else:
                    start = int(limits[0])
                    end = int(limits[1])
            slices.append((start, end))
        return slices
