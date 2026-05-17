from queue import Queue
from queue import Empty

q = Queue()

try:
    print(q.get(block=True, timeout=5))  # This will wait at most 5 seconds for an item
except Empty:
    print("No item was available within the timeout period")

try:
    print(q.get(block=False))  # This will raise Empty if no item is immediately available
except Empty:
    print("No item was available")