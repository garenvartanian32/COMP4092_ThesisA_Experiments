def can_access_invoice(invoice, user, access_code):
    if user == invoice.user or access_code == invoice.user.access_code:
        return True
    else:
        return False
