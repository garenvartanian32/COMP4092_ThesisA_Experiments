def results(self):
    return {'total': self.total, 'passed': self.total_passed, 'failed': self.total_failed, 'skipped': self.total_skipped, 'error': self.total_error, 'duration': self.duration}