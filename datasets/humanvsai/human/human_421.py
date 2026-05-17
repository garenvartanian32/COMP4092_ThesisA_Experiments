def _get_day_of_month(other, day_option):
    if day_option == 'start':
        return 1
    elif day_option == 'end':
        days_in_month = _days_in_month(other)
        return days_in_month
    elif day_option is None:
        # Note: unlike `_shift_month`, _get_day_of_month does not
        # allow day_option = None
        raise NotImplementedError
    else:
        raise ValueError(day_option)