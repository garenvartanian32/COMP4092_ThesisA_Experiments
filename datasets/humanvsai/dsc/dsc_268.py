class Checker:
    # Define some status constants
    STATUS_OK = 0
    STATUS_ERROR = 1

    def run(self, data):
        # Here you would implement your check logic
        # For example, let's say we're checking if the data is an instance of DSM, DMM, or MDM
        if isinstance(data, (DSM, DMM, MDM)):
            return (Checker.STATUS_OK, "Data is an instance of DSM, DMM, or MDM")
        else:
            return (Checker.STATUS_ERROR, "Data is not an instance of DSM, DMM, or MDM")