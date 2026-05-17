def find_day_in_month(other, day_option):
    if day_option == 'start':
        return 1
    elif day_option == 'end':
        import calendar
        return calendar.monthrange(other.year, other.month)[1]
