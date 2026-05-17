import asyncio

async def create_futures(address_values):
    loop = asyncio.get_running_loop()
    futures = []
    for address, value in address_values:
        futures.append(loop.run_in_executor(None, lambda: (address, value)))
    return futures
