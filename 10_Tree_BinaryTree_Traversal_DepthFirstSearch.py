class Node():
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)
    
    def preorder(self, start, traversal):
        #Value , Left, Right
        
        if start is None : 
            return
        traversal.append(start.value)
        self.preorder(start.left , traversal)
        self.preorder(start.right , traversal)
        
        return traversal       
        
        
    def inorder(self, start, traversal):
        #Left , Value , Right
        
        if start is None:
            return
        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)
        
        return traversal
        
        
    def postorder(self, start, traversal):
        # left, Right, Value
        
        if start is None:
            return
        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)
        
        return traversal

tree = BinaryTree(50)

tree.root.left = Node(10)
tree.root.left.left = Node(55)
tree.root.left.right = Node(80)

tree.root.right = Node(90)
tree.root.right.left = Node(44)
tree.root.right.right = Node(60)

resultPreorder = tree.preorder(tree.root , [])
print("Preorder: ",resultPreorder)

resultInorder = tree.inorder(tree.root , [])
print("Inorder: ",resultInorder)

resultPostorder = tree.postorder(tree.root , [])
print("Postorder: ",resultPostorder)


        