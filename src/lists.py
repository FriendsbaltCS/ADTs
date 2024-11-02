class OrderedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        # Insert item in sorted order
        self.items.append(item)
        self.items.sort()

    def remove(self, item):
        self.items.remove(item)

    def get(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)

class UnorderedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def get(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)