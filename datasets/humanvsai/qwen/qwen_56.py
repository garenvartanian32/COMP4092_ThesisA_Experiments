def get_sourced_from(entry):
    if 'source_from' in entry:
        return entry['source_from']
    else:
        return []
entry = {'source_from': ['database', 'api']}