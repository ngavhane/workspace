"""
Algorithms:

1. Do a level traversal of the tree and check which node has its left child
and right child as None and then just return count of such nodes.

This algorithm implemented by get_leaf_count_from_tree() method

2. A node is a leaf node if both left and right child nodes of it are NULL.

Here is an algorithm to get the leaf node count.

getLeafCount(node)
1) If node is NULL then return 0.
2) Else If left and right child nodes are NULL return 1.
3) Else recursively calculate leaf count of the tree using below formula.
    Leaf count of a tree = Leaf count of left subtree +
                                 Leaf count of right subtree









"""












class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SList(object):
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        if self.head is None:
            self.head = Node(data=data)
            return
        temp = self.head
        self.head = Node(data=data)
        self.head.next = temp

    def delete_at_last(self):
        temp_succ = None
        temp = self.head
        if temp.next is None:
            element = temp.data
            self.head = None
        else:
            while temp.next:
                temp_succ = temp
                temp = temp.next
            element = temp.data
            if temp_succ is not None:
                temp_succ.next = None
        return element

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def is_slist_empty(self):
        return True if self.head is None else False

class Queue(object):
    def __init__(self):
        self.slist = SList()

    def enqueue(self, element):
        self.slist.insert_at_beg(element)

    def dequeue(self):
        return self.slist.delete_at_last()

    def print_queue_from_front_to_rear(self):
        self.slist.print_list()

    def is_queue_empty(self):
        return self.slist.is_slist_empty()


#   Above code is for queue implementation


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

    def get_leaf_count_from_tree(self, root):
        leaf_count = 0
        queue = Queue()
        if root is not None:
            queue.enqueue(root)
        while not queue.is_queue_empty():
            node = queue.dequeue()
            if node.left is None and node.right is None:
                leaf_count = leaf_count + 1
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return leaf_count

    def get_leaf_node_count_using_recursive_approach(self, root):
        if root is None:
            return 0
        if root.left is None and root.left is None:
            return 1
        else:
            return \
                self.get_leaf_node_count_using_recursive_approach(root.left) + \
                self.get_leaf_node_count_using_recursive_approach(root.right)





bst = BstTree(10)
bst.insert_node(bst.root, 9)
bst.insert_node(bst.root, 15)
bst.insert_node(bst.root, 11)
bst.insert_node(bst.root, 17)
bst.insert_node(bst.root, 7)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, -9)
print "****** In order traversal of the tree is ****"
bst.inorder_traversal(bst.root)
print "****** Number of leaf node of the tree is :"
print bst.get_leaf_count_from_tree(bst.root)

print "****** Number of leaf node of the tree is :"
print bst.get_leaf_node_count_using_recursive_approach(bst.root)

