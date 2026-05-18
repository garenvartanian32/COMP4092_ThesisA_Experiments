class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, key):
        index = self._hash(key)

        while True:
            item = self.table[index]

            if item is None or item[0] == key:
                return index

            index = (index + 1) % self.size

    def set(self, key, value):
        if (self.count + 1) / self.size > 0.7:
            self._resize()

        index = self._probe(key)

        if self.table[index] is None:
            self.count += 1

        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        checked = 0

        while checked < self.size:
            item = self.table[index]

            if item is None:
                return None

            if item[0] == key:
                return item[1]

            index = (index + 1) % self.size
            checked += 1

        return None

    def _resize(self):
        old_items = []

        for item in self.table:
            if item is not None:
                old_items.append(item)

        self.size *= 2
        self.count = 0
        self.table = [None] * self.size

        for key, value in old_items:
            self.set(key, value)


def hash_juggling(pairs):
    table = HashTable()

    for key, value in pairs:
        table.set(key, value)

    return table
