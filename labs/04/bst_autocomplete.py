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
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def autocomplete(self, prefix):
        result = []

        def _inorder(node: Node | None):
            if node is None:
                return
            prefix2 = node.key[0:min(len(node.key), len(prefix))]
            # TODO: Traverse left subtree
            if prefix2 >= prefix:
                _inorder(node.left)
            # TODO: If node.key starts with prefix, add to result
            if prefix2 == prefix:
                result.append(node.key)
            # TODO: Traverse right subtree
            if prefix2 <= prefix:
                _inorder(node.right)

        _inorder(self.root)
        return result


def main():
    try:
        if sys.stdin.isatty():
            print("Enter prefix: ")
            prefix = input().strip()
            print("Enter the words of the tree separated by spaces: ")
            words = input().strip().split()
        else:
            print("Enter prefix: ", end="")
            input_lines = sys.stdin.read().strip().split("\n")
            if len(input_lines) >= 2:
                prefix = input_lines[0].strip()
                print("Enter the words of the tree separated by spaces: ", end="")
                words = input_lines[1].strip().split()
            else:
                print("Insufficient input provided.")
                return
    except Exception:
        print("Error reading input.")
        return

    tree = BST()
    for word in words:
        tree.insert(word.lower())

    matches = tree.autocomplete(prefix.lower())
    print(f"Autocomplete results for prefix '{prefix}':")
    for word in matches:
        print(word)


if __name__ == "__main__":
    main()
