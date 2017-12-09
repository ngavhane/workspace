"""
Given a binary tree, print level order traversal in a way that nodes of all levels are printed in separate lines.

For example consider the following tree

          1
       /     \
      2       3
    /   \       \
   4     5       6
        /  \     /
       7    8   9

Output for above tree should be
1
2 3
4 5 6
7 8 9



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

    def get_level_of_node(self, root, data):
        queue = Queue()
        node_list = []
        height = 0
        count = 1
        if root is not None:
            queue.enqueue(root)
        while not queue.is_queue_empty():
            height = height + 1
            x = count
            for i in range(x):
                node_list.append(queue.dequeue())
                count = count - 1
            for node in node_list:
                if node.data == data:
                    return height
            for node in node_list:
                if node.left is not None:
                    count = count + 1
                    queue.enqueue(node.left)
                if node.right is not None:
                    count = count + 1
                    queue.enqueue(node.right)
            node_list = []
        return " '%s' Node does not exist in the tree" % data



bst = BstTree(10)
bst.insert_node(bst.root, 9)
bst.insert_node(bst.root, 15)
bst.insert_node(bst.root, 11)
bst.insert_node(bst.root, 17)
bst.insert_node(bst.root, 7)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, -9)
bst.insert_node(bst.root, 100)
print "****** In order traversal of the tree is ****"
bst.inorder_traversal(bst.root)
print "****** Height of 100 node is :"
print bst.get_level_of_node(bst.root, 100)
print "****** Height of 90 node is :"
print bst.get_level_of_node(bst.root, 90)

