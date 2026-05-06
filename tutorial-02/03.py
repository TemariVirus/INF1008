class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next: SinglyListNode | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, value):
        node = SinglyListNode(value)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def deleteHead(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def print(self):
        print("[", end=" ")
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("]")


class MyQueue:
    def __init__(self):
        self.items = SinglyLinkedList()

    def enqueue(self, value):
        self.items.insertTail(value)

    def printQueue(self):
        self.items.print()

    def dequeue(self):
        return self.items.deleteHead()

    def peek(self):
        if self.items.head is None:
            print("Queue is empty, nothing to peek.")
            return
        return self.items.head.data


if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.printQueue()
    assert q.dequeue() == 1
    assert q.peek() == 2
    assert q.dequeue() == 2
    assert q.dequeue() == 3
