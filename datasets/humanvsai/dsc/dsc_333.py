import concurrent.futures

def worker(key):
    # do some work
    pass

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_key = {executor.submit(worker, key): key for key in range(20)}
    for future in concurrent.futures.as_completed(future_to_key):
        key = future_to_key[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (key, exc))
        else:
            print('%r page is %d bytes' % (key, len(data)))