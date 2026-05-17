import zlib

def data_blocks(data: bytes):
    start = 0
    while True:
        # Find the next IDAT chunk
        index = data.find(b'IDAT', start)
        if index == -1:
            break

        # Get the compressed data
        start = index + 4
        length = int.from_bytes(data[start:start+4], byteorder='big')
        compressed_data = data[start+4:start+4+length]

        # Decompress the data and yield
        decompressed_data = zlib.decompress(compressed_data)
        yield decompressed_data
