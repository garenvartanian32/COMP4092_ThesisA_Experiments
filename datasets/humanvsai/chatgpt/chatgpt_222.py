def add_record_class(cls):
    record_store = []
    
    def wrapper(*args, **kwargs):
        record = cls(*args, **kwargs)
        record_store.append(record)
        return record
    
    wrapper.record_store = record_store
    return wrapper
