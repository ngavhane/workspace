"""
We have discussed BST search and insert operations. In this post, delete operation is discussed.
 When we delete a node, there possibilities arise.

1) Node to be deleted is leaf: Simply remove from the tree.

              50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70
         /  \    /  \                     \    /  \
       20   40  60   80                   40  60   80
2) Node to be deleted has only one child: Copy the child to the node and delete the child

              50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70
            \    /  \                          /  \
            40  60   80                       60   80
3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of
the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.

              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70
                 /  \                            \
                60   80                           80
The important thing to note is, inorder successor is needed only when right child is not empty.
In this particular case, inorder successor can be obtained by finding the minimum value in right child of the node.


"""


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

    def delete_node(self, root, data):
        if root.data < data:
            self.delete_node(root.right, data)
        elif root.data > data:
            self.delete_node(root.left, data)
        else:
            if root.left is None and root.right is None:
                print "I am here"
                print root.data
                root = None

    def search_node(self, root, data):
        if root is None:
            print "Element does not exist"
        elif root.data == data:
            print "Element exist"
        elif root.data < data:
            self.search_node(root.right, data)
        elif root.data > data:
            self.search_node(root.left, data)


bst = BinarySearchTree(20)
bst.insert_node(bst.root, 1)
bst.insert_node(bst.root, 3)
bst.insert_node(bst.root, 4)
bst.insert_node(bst.root, 30)
bst.insert_node(bst.root, 100)
bst.insert_node(bst.root, 500)
bst.insert_node(bst.root, 0)
bst.insert_node(bst.root, -9)
bst.in_order_print_tree(bst.root)
bst.delete_node(bst.root, 4)
print "****"
bst.in_order_print_tree(bst.root)

