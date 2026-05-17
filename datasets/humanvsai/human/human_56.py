def get_sourced_from(entry):
    sourced_from = 'http://worldmodelers.com/DataProvenance#sourced_from'
    if sourced_from in entry:
        values = entry[sourced_from]
        values = [i['@id'] for i in values]
        return values