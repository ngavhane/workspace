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

    def check_if_two_trees_are_equal(self, first, second):
        if first is None and second is None:
            return True
        if first is not None and second is not None:
            return ((first.data == second.data) and
                self.check_if_two_trees_are_equal(first.left, second.left)and
                self.check_if_two_trees_are_equal(first.right, second.right))
        return False



bst = BstTree(10)
bst.insert_node(bst.root, 9)
bst.insert_node(bst.root, 15)
bst.insert_node(bst.root, 7)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, -9)
bst.insert_node(bst.root, 21)


bst1 = BstTree(10)
bst1.insert_node(bst1.root, 9)
bst1.insert_node(bst1.root, 15)
bst1.insert_node(bst1.root, 7)
bst1.insert_node(bst1.root, 50)
bst1.insert_node(bst1.root, -9)
bst1.insert_node(bst1.root, 21)


if bst.check_if_two_trees_are_equal(bst.root, bst1.root):
    print "Both trees are identical"
else:
    print "Trees are not identical"




