def valid_daily_max_min_temperature(comp, units='K'):
    def wrapper(func):
        def inner_func(*args, **kwargs):
            # Assuming that the first argument is the temperature dataset
            temperature_dataset = args[0]
            
            # Check if the dataset is valid
            if not is_valid_temperature_dataset(temperature_dataset):
                raise ValueError("Invalid temperature dataset")
            
            # If the dataset is valid, run the computation
            return func(*args, **kwargs)
        return inner_func
    return wrapper

def is_valid_temperature_dataset(dataset):
    # Add your own logic to check if the dataset is valid
    # For example, you might check if the dataset is a list or tuple,
    # if it has at least one element, and if all elements are numbers
    return isinstance(dataset, (list, tuple)) and len(dataset) > 0 and all(isinstance(x, (int, float)) for x in dataset)

# Usage
@valid_daily_max_min_temperature
def compute_average_temperature(temperature_dataset):
    return sum(temperature_dataset) / len(temperature_dataset)

# This will raise a ValueError
try:
    print(compute_average_temperature([]))
except ValueError as e:
    print(e)

# This will print the average temperature
print(compute_average_temperature([273.15, 283.15, 293.15]))