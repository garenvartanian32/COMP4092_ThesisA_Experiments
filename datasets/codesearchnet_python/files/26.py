def _check_series_convert_timestamps_localize(s, from_timezone, to_timezone):
    """
    Convert timestamp to timezone-naive in the specified timezone or local timezone

    :param s: a pandas.Series
    :param from_timezone: the timezone to convert from. if None then use local timezone
    :param to_timezone: the timezone to convert to. if None then use local timezone
    :return pandas.Series where if it is a timestamp, has been converted to tz-naive
    """
    from pyspark.sql.utils import require_minimum_pandas_version
    require_minimum_pandas_version()

    import pandas as pd
    from pandas.api.types import is_datetime64tz_dtype, is_datetime64_dtype
    from_tz = from_timezone or _get_local_timezone()
    to_tz = to_timezone or _get_local_timezone()
    # TODO: handle nested timestamps, such as ArrayType(TimestampType())?
    if is_datetime64tz_dtype(s.dtype):
        return s.dt.tz_convert(to_tz).dt.tz_localize(None)
    elif is_datetime64_dtype(s.dtype) and from_tz != to_tz:
        # `s.dt.tz_localize('tzlocal()')` doesn't work properly when including NaT.
        return s.apply(
            lambda ts: ts.tz_localize(from_tz, ambiguous=False).tz_convert(to_tz).tz_localize(None)
            if ts is not pd.NaT else pd.NaT)
    else:
        return s