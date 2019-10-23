class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Hello")
    q.enqueue("Dog")
    q.enqueue(3)
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())

