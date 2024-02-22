class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self, item):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self, item):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
