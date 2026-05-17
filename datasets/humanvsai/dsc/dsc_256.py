import zlib

def decompress(data_blocks):
    decompressor = zlib.decompressobj()
    for block in data_blocks:
        yield decompressor.decompress(block)