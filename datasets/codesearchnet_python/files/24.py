def _check_dataframe_localize_timestamps(pdf, timezone):
    """
    Convert timezone aware timestamps to timezone-naive in the specified timezone or local timezone

    :param pdf: pandas.DataFrame
    :param timezone: the timezone to convert. if None then use local timezone
    :return pandas.DataFrame where any timezone aware columns have been converted to tz-naive
    """
    from pyspark.sql.utils import require_minimum_pandas_version
    require_minimum_pandas_version()

    for column, series in pdf.iteritems():
        pdf[column] = _check_series_localize_timestamps(series, timezone)
    return pdf