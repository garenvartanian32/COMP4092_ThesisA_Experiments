def round(self, ndigits=0):
    return self.quantize(Decimal('1.' + '0' * ndigits), rounding=ROUND_HALF_UP)