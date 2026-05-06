class Stack:
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, value):
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        value = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return value

    def isEmpty(self):
        return self.top < 0

    def peek(self):
        return self.data[self.top]

    def print(self):
        print(self.top)
        print(self.data)

    def invert(self):
        for i in range(len(self.data) // 2):
            j = len(self.data) - i - 1
            self.data[i], self.data[j] = self.data[j], self.data[i]


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(1)
    s.invert()
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
