class HashTable():
    def __init__(self, size, slots, values):
        self.size = size
        self.slots = [None] * len(slots)
        self.values = [None] * len(values)

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass


h = HashTable()
h[45] = "nitin"
print h[45]