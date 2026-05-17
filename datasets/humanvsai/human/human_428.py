def _getDevMajorMinor(self, devpath):
        fstat = os.stat(devpath)
        if stat.S_ISBLK(fstat.st_mode):
            return(os.major(fstat.st_rdev), os.minor(fstat.st_rdev))
        else:
            raise ValueError("The file %s is not a valid block device." % devpath)