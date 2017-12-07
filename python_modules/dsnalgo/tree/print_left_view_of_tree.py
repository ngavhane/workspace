"""
Algorithm:

for any traversal algorithm pass root.left instead of root.

"""




class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, data):
        self.root = Node(data)

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print root.data
        self.inorder_traversal(root.right)


t = Tree(10)
t.root.left = Node(4)
t.root.left.right = Node(7)
t.root.left.right.right = Node(8)
t.root.right = Node(20)

t.inorder_traversal(t.root)

print "Print left side of the tree is"
t.inorder_traversal(t.root.left)

