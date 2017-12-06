


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

    def get_height_of_tree(self, root):

        if root is not None:
            return 1 + max(self.get_height_of_tree(root.left), self.get_height_of_tree(root.right))
        else:
            return 0

    def print_nodes_of_specific_level(self, root, level):
        if root is None:
            return
        elif level == 1:
            print root.data
            return
        else:
            self.print_nodes_of_specific_level(root.left, level-1)
            self.print_nodes_of_specific_level(root.right, level-1)

    def level_order_traversal_of_tree(self, root):

        height = self.get_height_of_tree(root=root)
        for i in range(1, height+1, 1):
            self.print_nodes_of_specific_level(root=root, level=i)

bst = BstTree(10)
bst.insert_node(bst.root, 9)
bst.insert_node(bst.root, 15)
bst.insert_node(bst.root, 11)
bst.insert_node(bst.root, 17)
bst.insert_node(bst.root, 7)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, -9)
bst.insert_node(bst.root, -90)
print "****** In order traversal of the tree is ****"
bst.inorder_traversal(bst.root)
print "****** Height of the tree is :"
height = bst.get_height_of_tree(bst.root)

print "Level order traversal of the tree is"
bst.level_order_traversal_of_tree(bst.root)




