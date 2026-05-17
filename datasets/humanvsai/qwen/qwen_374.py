def check(self):
    records = self.get_records()
    ready_records = [record for record in records if record.is_ready()]
    if ready_records:
        return tuple(ready_records)
    else:
        return None