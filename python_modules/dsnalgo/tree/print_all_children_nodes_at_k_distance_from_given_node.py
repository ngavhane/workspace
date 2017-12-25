"""
Given a binary tree, a target node in the binary tree, and an integer value k,
print all the nodes that are at distance k from the given target node. No parent pointers are available.


             20
            /  \
          8    22
        /  \
       4   12
          /  \
        10   14
BinaryTree

Consider the tree shown in diagram

Input: target = pointer to node with data 8.
       root = pointer to node with data 20.
       k = 2.
Output : 10 14 22

If target is 14 and k is 3, then output
should be "4 20"



Algorithm:

use logic of printing nodes level by level, where each level is in one line

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

    def level_order_traversal_of_tree_using_queue(self, root):
        queue = Queue()
        if root is not None:
            queue.enqueue(root)
        while not queue.is_queue_empty():
            node = queue.dequeue()
            print node.data
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

    def level_order_traversal_of_tree_using_queue_line_by_line(self, root):
        queue = Queue()
        node_list = []
        count = 1
        if root is not None:
            queue.enqueue(root)
        while not queue.is_queue_empty():
            x = count
            for i in range(x):
                node_list.append(queue.dequeue())
                count = count - 1
            print(' '.join(str(x.data) for x in node_list))
            for node in node_list:
                if node.left is not None:
                    count = count + 1
                    queue.enqueue(node.left)
                if node.right is not None:
                    count = count + 1
                    queue.enqueue(node.right)
            node_list = []

    def print_all_childrens_at_k_distance_from_given_node(self, node, k):
        queue = Queue()
        node_list = []
        count = 1
        level_from_given_node = 0

        queue.enqueue(node)
        while not queue.is_queue_empty():
            x = count
            for i in range(x):
                node_list.append(queue.dequeue())
                count = count - 1
            if level_from_given_node == k:
                print(' '.join(str(x.data) for x in node_list))
            for node in node_list:
                if node.left is not None:
                    count = count + 1
                    queue.enqueue(node.left)
                if node.right is not None:
                    count = count + 1
                    queue.enqueue(node.right)
            node_list = []
            level_from_given_node = level_from_given_node + 1





bst = BstTree(20)
bst.insert_node(bst.root, 8)
bst.insert_node(bst.root, 22)
bst.insert_node(bst.root, 4)
bst.insert_node(bst.root, 12)
bst.insert_node(bst.root, 10)
bst.insert_node(bst.root, 14)
bst.insert_node(bst.root, 11)
bst.insert_node(bst.root, 13)
bst.insert_node(bst.root, 16)
bst.insert_node(bst.root, 3)
bst.insert_node(bst.root, 1)
print "****** In order traversal of the tree is ****"
bst.inorder_traversal(bst.root)
print "****** Level Order traversal of the tree is :"
bst.level_order_traversal_of_tree_using_queue(bst.root)
print "****** Level Order traversal of the tree line by line is :"
bst.level_order_traversal_of_tree_using_queue_line_by_line(bst.root)

print "****** Nodes at k distance from a given node"
bst.print_all_childrens_at_k_distance_from_given_node(bst.root.left.right, k=2)






