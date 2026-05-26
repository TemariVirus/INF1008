class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    brackets = Stack()
    pairs = [
        ("(", ")"),
        ("[", "]"),
        ("{", "}"),
    ]
    for c in input():
        for open, close in pairs:
            if c == open:
                brackets.push(c)
                break
            elif c == close:
                if brackets.is_empty():
                    print("Not legal")
                    exit()
                other = brackets.pop()
                if other != open:
                    print("Not legal")
                    exit()
                break

    if not brackets.is_empty():
        print("Not legal")
        exit()

    print("Legal")
