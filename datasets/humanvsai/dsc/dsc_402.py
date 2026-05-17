def IsFileRequired(self, filename):
    # List of required files in GTFS
    required_files = ['agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt']

    # Check if the file is in the list of required files
    if filename in required_files:
        return True
    else:
        return False