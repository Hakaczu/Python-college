class Stack:

    def __init__(self):
        self.items = {}

    def push(self, item):
        position = len(self.items)
        self.items[position+1] = item

    def top(self):
        position = len(self.items)
        return self.items[position]

    def height(self):
        return len(self.items)

    def pop(self):
        if len(self.items) == 0:
            raise ValueError("Stack is empty")
        else:
            position = len(self.items)
            value = self.items[position]
            del self.items[position]
            return value