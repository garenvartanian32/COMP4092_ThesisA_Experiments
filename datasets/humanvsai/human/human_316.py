def iter_regions(self):
        # TODO: Implement BoundingBox
        # TODO: Implement sort order
        for x,z in self.regionfiles.keys():
            close_after_use = False
            if (x,z) in self.regions:
                regionfile = self.regions[(x,z)]
            else:
                # It is not yet cached.
                # Get file, but do not cache later.
                regionfile = region.RegionFile(self.regionfiles[(x,z)], chunkclass = self.chunkclass)
                regionfile.loc = Location(x=x,z=z)
                close_after_use = True
            try:
                yield regionfile
            finally:
                if close_after_use:
                    regionfile.close()