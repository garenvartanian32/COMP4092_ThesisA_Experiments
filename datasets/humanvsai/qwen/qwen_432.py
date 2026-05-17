def _assemble_influence(stmt):
    if not stmt:
        return ''
    if isinstance(stmt, str):
        return stmt
    if isinstance(stmt, list):
        return ' '.join((_assemble_influence(s) for s in stmt))
    if isinstance(stmt, dict):
        return ' '.join((f'{k}: {_assemble_influence(v)}' for (k, v) in stmt.items()))
    raise ValueError('Unsupported type for Influence statement')

def _assemble_influence_test():
    """Test the _assemble_influence function."""
    assert _assemble_influence('') == ''
    assert _assemble_influence('Hello') == 'Hello'
    assert _assemble_influence(['Hello', 'World']) == 'Hello World'
    assert _assemble_influence({'key': 'value'}) == 'key: value'
    assert _assemble_influence({'key': ['nested', 'list']}) == 'key: nested list'
    assert _assemble_influence({'key': {'nested': 'value'}}) == 'key: nested: value'
    assert _assemble_influence([{'key': 'value'}, 'string', ['list', 'of', 'strings']]) == 'key: value string list of strings'
    print('All tests passed.')