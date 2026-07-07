import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def find(self, key):
        def _find(node, key):
            if node is None or node.key == key:
                return node
            return _find(node.left, key) if key < node.key else _find(node.right, key)

        return _find(self.root, key)


    def printTree(self, node=None, level=0, prefix="Root: "):
        # Only set to self.root on the *initial* call
        if node is None and level == 0:
            node = self.root
        if node is None:
            return

        self.printTree(node.right, level + 1, "R--- ")
        print(" " * (level * 4) + prefix + node.key)
        self.printTree(node.left, level + 1, "L--- ")

    def countDecendants(self, node: Node | None, level: int) -> int:
        if node is None or level < 0:
            return 0
        if level == 0:
            return 1
        return self.countDecendants(node.left, level - 1) + self.countDecendants(
            node.right, level - 1
        )

    def getLevelNodesCount(self, k):
        # TODO Implement this method            
        return self.countDecendants(self.root, k)

def main():
    try:
        if sys.stdin.isatty():
            print("Enter depth: ")
            k = int(input().strip())
            print("Enter the keys of the tree separated by spaces: ")
            keys = input().strip().split()
        else:
            print("Enter depth: ", end="")
            input_lines = sys.stdin.read().strip().split('\n')
            if len(input_lines) >= 2:
                k = int(input_lines[0].strip())
                print("Enter the keys of the tree separated by spaces: ", end="")
                keys = input_lines[1].strip().split()
            else:
                print("Insufficient input provided.")
                return
    except Exception:
        print("Error reading input.")
        return


    # Create BST and insert nodes
    tree = BST()

    for key in keys:
        tree.insert(key)

    #tree.printTree()

    # Get level nodes count for depth "k"
    print(f"Count of nodes at depth {k}: {tree.getLevelNodesCount(k)}")


if __name__ == "__main__":
    main()


r'''
['F', 'D', 'I', 'C', 'E', 'G', 'J', 'B', 'H', 'A']
           F
	    /     \
       D       I
      / \     / \
     C   E   G   J
    /         \
   B           H
  /
 A 
'''
