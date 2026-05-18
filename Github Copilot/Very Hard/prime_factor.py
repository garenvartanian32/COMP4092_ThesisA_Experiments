def prime_factors(n):
    factors = []
    # Divide by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors