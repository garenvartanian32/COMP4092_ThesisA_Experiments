def names2dnsrepr(x):
    if isinstance(x, list):
        return '.'.join(x)
    elif isinstance(x, str):
        return x
    else:
        raise ValueError("Input must be a list of DNS names or a single DNS name")

# Test the function
print(names2dnsrepr(["www", "google", "com"]))  # Output: www.google.com
print(names2dnsrepr("www.google.com"))  # Output: www.google.com