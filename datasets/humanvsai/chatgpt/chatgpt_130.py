import mmap

def communicate_with_pageant():
    # Open a shared memory-mapped file for read and write access
    with mmap.mmap(-1, 1024, tagname='pageant_shared_mem') as mem:
        # Read data from the shared memory
        data = mem.read(1024)
        
        # Write data to the shared memory
        mem.write(b'Hello from the pageant process!')
