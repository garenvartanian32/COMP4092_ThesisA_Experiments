def validate_business(form, field):
    if not form.data.get(field):
        return False
    value = form.data.get(field)
    if '@' in value:
        return validate_email(value)
    else:
        return validate_paypal_id(value)

def validate_email(email):
    """Validates an email address."""
    import re
    pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_paypal_id(paypal_id):
    """Validates a PayPal business account ID."""
    import re
    pattern = '^[A-Z0-9]{13}$'
    return re.match(pattern, paypal_id) is not None