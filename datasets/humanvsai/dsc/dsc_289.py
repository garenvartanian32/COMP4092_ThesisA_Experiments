import concurrent.futures

def create_initial(self, address_values):
    """Create futures from inputs with the current value for that address
    at the start of that context.

    Args:
        address_values (list of tuple): The tuple is string, bytes of the
            address and value.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(self.get_value, address): address for address, _ in address_values}

    for future in concurrent.futures.as_completed(futures):
        address = futures[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (address, exc))
        else:
            print('%r page is %d bytes' % (address, len(data)))