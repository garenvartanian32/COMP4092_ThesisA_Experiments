from decimal import Decimal, ROUND_HALF_UP

def round_decimal(amount: float) -> Decimal:
    decimal_amount = Decimal(amount)
    rounded_amount = decimal_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return rounded_amount
