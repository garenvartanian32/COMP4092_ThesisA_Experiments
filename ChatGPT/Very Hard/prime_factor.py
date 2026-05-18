def express_factors(n):
    factors = {}
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    parts = []

    for factor in sorted(factors):
        power = factors[factor]

        if power == 1:
            parts.append(str(factor))
        else:
            parts.append(str(factor) + "^" + str(power))

    return " x ".join(parts)
