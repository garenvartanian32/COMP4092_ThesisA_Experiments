def writeNSdict(self, nsdict):
    """Write a namespace dictionary, taking care to not clobber the
        standard (or reserved by us) prefixes."""

    # Define your reserved prefixes
    reserved_prefixes = ['reserved_prefix1', 'reserved_prefix2', 'reserved_prefix3']

    for key, value in nsdict.items():
        if key not in reserved_prefixes:
            # Write the key-value pair to your desired output
            print(f'{key}: {value}')