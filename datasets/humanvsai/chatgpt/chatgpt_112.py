import re

def validate_paypal_business_string(paypal_str):
    if not isinstance(paypal_str, str):
        return False
    if re.fullmatch(r'\w+[-+.]*\w+@\w+[-.]*\w+\.\w+', paypal_str):
        return True
    elif re.fullmatch(r'^[A-Z0-9]{13}$', paypal_str):
        return True
    else:
        return False
