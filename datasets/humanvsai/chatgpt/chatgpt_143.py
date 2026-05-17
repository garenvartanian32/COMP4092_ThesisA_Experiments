def temperature_range_check(computation_func):
    def wrapper(min_temperature, max_temperature):
        if min_temperature < -273.15:
            raise ValueError("Minimum temperature cannot be less than -273.15°C")
        if max_temperature < -273.15:
            raise ValueError("Maximum temperature cannot be less than -273.15°C")
        if min_temperature > max_temperature:
            raise ValueError("Minimum temperature cannot be greater than maximum temperature")
        result = computation_func(min_temperature, max_temperature)
        return result
    return wrapper
