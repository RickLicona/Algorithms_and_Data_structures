class Stack:
    # The top is at the beginning instead of at the end
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push('Hello')
    s.push('True')
    print(s.pop())

