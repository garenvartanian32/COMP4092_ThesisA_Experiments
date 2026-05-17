class ValidationError(Exception):
    pass

def validate_language(obj):
    for key, value in obj.items():
        if key == "language":
            if not isinstance(value, str):
                raise ValidationError("Language should be a string")
            # Add more conditions to validate language string as required
        elif isinstance(value, dict):
            validate_language(value)
