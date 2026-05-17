def _listlike_guard(obj, name, iterable_only=False, log_warning=True):
  required_type = (_Iterable,) if iterable_only else (_Container, _Iterable)
  required_type_name = ' or '.join(t.__name__ for t in required_type)
  if not isinstance(obj, required_type):
    raise ValueError('{} must be of type {}'.format(name, required_type_name))
  # at this point it is definitely the right type, but might be a string
  if isinstance(obj, basestring):
    if log_warning:
      _logger.warning('{} passed as a string; should be list-like'.format(name))
    return (obj,)
  return obj