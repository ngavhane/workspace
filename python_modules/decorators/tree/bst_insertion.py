class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self, data):
        self.root = Tree(data)

    def insert_node(self, root, data):

        if data <= root.data:
            if root.left is None:
                root.left = Tree(data)
            else:
                self.insert_node(root.left, data)
        else:
            if root.right is None:
                root.right = Tree(data)
            else:
                self.insert_node(root.right, data)

    def in_order_print_tree(self, root):
        if root is None:
            return
        else:
            self.in_order_print_tree(root.left)
            print root.data
            self.in_order_print_tree(root.right)

    def pre_order_print_tree(self, root):
        if root is None:
            return
        else:
            print root.data
            self.pre_order_print_tree(root.left)
            self.pre_order_print_tree(root.right)

    def post_order_print_tree(self, root):
        if root is None:
            return
        else:
            self.post_order_print_tree(root.left)
            self.post_order_print_tree(root.right)
            print root.data


bst = BinarySearchTree(20)
bst.insert_node(bst.root, 1)
bst.insert_node(bst.root, 3)
bst.insert_node(bst.root, 4)
bst.insert_node(bst.root, 30)
bst.insert_node(bst.root, 100)
bst.insert_node(bst.root, 500)
bst.insert_node(bst.root, 0)
bst.insert_node(bst.root, -9)
print "**********************"
print "IN order traversal of the Binary Search tree is"
bst.in_order_print_tree(bst.root)
print "**********************"
print "Pre order traversal of the Binary Search tree is"
bst.pre_order_print_tree(bst.root)
print "**********************"
print "POST order traversal of the Binary Search tree is"
bst.post_order_print_tree(bst.root)
