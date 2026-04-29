class SharedMemory:
    def __init__(self):
        self.store = {"history": []}

    def set(self, key, value):
        self.store[key] = value
        self.store["history"].append((key, value))

    def get(self, key):
        return self.store.get(key)

    def history(self):
        return self.store["history"]
