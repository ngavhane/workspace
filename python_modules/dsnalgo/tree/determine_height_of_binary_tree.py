class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BstTree(object):
    def __init__(self, data):
        self.root = Tree(data)

    def insert_node(self, root, data):
        if root.data >= data:
            if root.left is None:
                root.left = Tree(data)
            else:
                self.insert_node(root.left, data)
        elif root.data < data:
            if root.right is None:
                root.right = Tree(data)
            else:
                self.insert_node(root.right, data)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print root.data
        self.inorder_traversal(root.right)

    def determine_height_of_tree(self, root):
        if root is not None:
            return (1 + max(self.determine_height_of_tree(root.left), self.determine_height_of_tree(root.right)))
        else:
            return 0

    def determine_height_of_node(self, root, data):
        if root.data == data:
            return (1 + max(self.determine_height_of_tree(root.left), self.determine_height_of_tree(root.right)))
        else:
            return 0

bst = BstTree(10)
print "******"
#bst.inorder_traversal(bst.root)
#bst.insert_node(bst.root, 9)
#bst.insert_node(bst.root, 8)
#bst.insert_node(bst.root, 7)
#bst.insert_node(bst.root, 50)
#bst.insert_node(bst.root, -9)
#bst.insert_node(bst.root, 21)
print "******"
bst.inorder_traversal(bst.root)

print "height of the tree "
print bst.determine_height_of_tree(bst.root)
print bst.determine_height_of_node(bst.root, 21)

