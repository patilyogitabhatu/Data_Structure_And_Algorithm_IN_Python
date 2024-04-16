class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)

tree = BinaryTree(5)

tree.root.left = Node(2)
tree.root.left.right = Node(6)
tree.root.left.left = Node(4)

tree.root.right = Node(3)
tree.root.right.left = Node(1)
tree.root.right.right = Node(7)        