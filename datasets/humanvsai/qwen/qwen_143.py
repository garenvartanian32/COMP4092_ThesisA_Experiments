def valid_daily_max_min_temperature(comp, units='K'):

    def decorator(func):

        def wrapper(*args, **kwargs):
            temp_data = kwargs.get('temp_data', None)
            if temp_data is None:
                raise ValueError('Temperature data is required.')
            if not isinstance(temp_data, dict) or 'max' not in temp_data or 'min' not in temp_data:
                raise ValueError("Temperature data must be a dictionary with 'max' and 'min' keys.")
            if units not in ['K', 'C', 'F']:
                raise ValueError("Units must be 'K', 'C', or 'F'.")
            if temp_data['max'] < temp_data['min']:
                raise ValueError('Max temperature must be greater than or equal to min temperature.')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@valid_daily_max_min_temperature(units='C')
def process_temperature_data(temp_data):
    print('Processing temperature data:', temp_data)