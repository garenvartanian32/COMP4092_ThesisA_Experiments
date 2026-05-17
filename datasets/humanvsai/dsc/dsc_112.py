import re

def validate_business(form, field):
    """Validates a PayPal business string.

    It can either be an email address or a PayPal business account ID.
    """
    # Regular expression pattern for email address
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # Regular expression pattern for PayPal business account ID
    paypal_pattern = r"(^[a-zA-Z0-9_-]+$)"

    if re.match(email_pattern, field):
        return True
    elif re.match(paypal_pattern, field):
        return True
    else:
        return False