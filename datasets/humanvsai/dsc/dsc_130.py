import mmap

def _query_pageant(msg):
    with open('shared_memory', 'r+b') as f:
        # memory-map the file, size 0 means the whole file
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(0)  # move to the start of the file
        mm.write(msg.encode())  # write the message to the shared memory
        mm.seek(0)  # move to the start of the file again
        print(mm.readline())  # read the message from the shared memory
        mm.close()  # close the map