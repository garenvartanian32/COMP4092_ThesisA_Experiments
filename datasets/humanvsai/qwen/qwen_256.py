def decompress(data_blocks):
    import zlib
    decompressor = zlib.decompressobj()
    for block in data_blocks:
        yield decompressor.decompress(block)