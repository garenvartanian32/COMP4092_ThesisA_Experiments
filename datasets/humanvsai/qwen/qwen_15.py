def check_hamster(self):
    self.hamster = self.load_hamster_data()
    self.last_activity = self.hamster.get('last_activity', None)
    self.current_time = datetime.now()
    self.time_since_last_activity = self.current_time - self.last_activity if self.last_activity else None
    self.refresh_interval = timedelta(seconds=self.refresh_interval_seconds)
    if self.time_since_last_activity and self.time_since_last_activity > self.refresh_interval:
        self.refresh_hamster_data()
    else:
        print('No need to refresh hamster data.')

def load_hamster_data(self):
    """Load hamster data from a file or database."""
    return {'last_activity': datetime.now() - timedelta(days=1)}

def refresh_hamster_data(self):
    """Refresh hamster data."""
    print('Hamster data refreshed.')
hamster_checker = HamsterChecker()
hamster_checker.refresh_interval_seconds = 3600