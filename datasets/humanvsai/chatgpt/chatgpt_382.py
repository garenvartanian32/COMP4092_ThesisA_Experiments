def set_span(span_list):
    """
    Sets the span for the term from list of ids
    @type span_list: []
    @param span_list: list of wf ids forming span
    """
    span = {'start': None, 'end': None}
    if span_list:
        span['start'] = span_list[0]
        span['end'] = span_list[-1]
    return span
