class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
            

class PotionStack(Stack):
    def push(self, potion):
        if self.peek() == potion:
            pass
        else:
            super().push(potion)


