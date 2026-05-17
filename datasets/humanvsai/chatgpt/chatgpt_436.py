def define_with_confidence(value, confidence_level):
    if value in defined_values:
        if defined_values[value] >= confidence_level:
            return
    defined_values[value] = confidence_level
