class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next: SinglyListNode | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, data):
        node = SinglyListNode(data)
        node.next = self.head
        self.head = node

    def print(self):
        print("[", end=" ")
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("]")


def mergeNonDecreasing(l1: SinglyLinkedList, l2: SinglyLinkedList):
    merged = SinglyLinkedList()
    node1 = l1.head
    node2 = l2.head
    if node1 is None and node2 is None:
        return merged
    elif node1 is None or (node2 is not None and node1.data > node2.data):
        merged.head = node2
        node2 = node2.next
    else:
        merged.head = node1
        node1 = node1.next

    node = merged.head
    while node1 is not None or node2 is not None:
        if node1 is None or (node2 is not None and node1.data > node2.data):
            node.next = node2
            node2 = node2.next
        else:
            node.next = node1
            node1 = node1.next
        node = node.next
    return merged


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.insertHead(50)
    l1.insertHead(45)
    l1.insertHead(45)
    l1.insertHead(10)
    l1.insertHead(6)
    l1.insertHead(6)
    l1.insertHead(3)
    l2 = SinglyLinkedList()
    l2.insertHead(60)
    l2.insertHead(55)
    l2.insertHead(3)
    l2.insertHead(2)

    merged = mergeNonDecreasing(l1, l2)
    merged.print()
