def IsFileRequired(self, filename):
    required_files = ['agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt']
    return filename in required_files