class OrderedList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.items.sort()

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def index(self, item):
        return self.items.index(item)

    def pop(self, pos=None):
        if pos is None:
            return self.items.pop()
        else:
            return self.items.pop(pos)

class UnorderedList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def search(self, item):
        return item in self.items

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def insert(self, pos, item):
        self.items.insert(pos, item)

    def pop(self, pos=None):
        if pos is None:
            return self.items.pop()
        else:
            return self.items.pop(pos)