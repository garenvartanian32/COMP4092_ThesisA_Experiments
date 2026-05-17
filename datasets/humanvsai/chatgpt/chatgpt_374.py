def check_ready_records() -> tuple:
    ready_records = [record for record in WScheduleRecord.objects.all() if record.is_ready()]
    return tuple(ready_records) if ready_records else None
