class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

class ArrayIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if self.has_next():
            value = self.items[self.position]
            self.position += 1
            return value
        raise StopIteration

if __name__ == "__main__":
    array = [1, 2, 3, 4]
    it = ArrayIterator(array)
    while it.has_next():
        print(it.next())
