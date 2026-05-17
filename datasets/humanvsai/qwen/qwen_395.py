def _ensure_valid_record_size(self, size):
    if size > self.max_record_size:
        raise ValueError(f'Record size {size} exceeds the maximum allowed size of {self.max_record_size}.')

def _ensure_valid_record_count(self, count):
    """Validate that the record count isn't too large."""
    if count > self.max_record_count:
        raise ValueError(f'Record count {count} exceeds the maximum allowed count of {self.max_record_count}.')

def _ensure_valid_record_data(self, data):
    """Validate that the record data is not empty and is of the correct type."""
    if not data:
        raise ValueError('Record data cannot be empty.')
    if not isinstance(data, (str, bytes)):
        raise TypeError('Record data must be of type str or bytes.')

def _ensure_valid_record(self, size, count, data):
    """Validate all aspects of a record."""
    self._ensure_valid_record_size(size)
    self._ensure_valid_record_count(count)
    self._ensure_valid_record_data(data)

def _ensure_valid_records(self, records):
    """Validate a list of records."""
    for record in records:
        self._ensure_valid_record(record['size'], record['count'], record['data'])
records = [{'size': 100, 'count': 1, 'data': 'example data'}, {'size': 200, 'count': 2, 'data': b'example bytes'}]
max_record_size = 500
max_record_count = 10