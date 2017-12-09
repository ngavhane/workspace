"""
Algorithm:

for any traversal algorithm pass root.left instead of root.

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




class TNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, data):
        self.root = TNode(data)

    def get_closest_leaf_from_a_node(self, root):
        queue = Queue()
        if root is not None:
            queue.enqueue(root)
        while not queue.is_queue_empty():
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            if node.left is None and node.right is None:
                return node.data

    def get_height_of_node(self, root, data, k=0):
        if root is None:
            return k
        elif root.data == data:
            print k
        else:
            self.get_height_of_node(root.left, data, k=k+1)
            self.get_height_of_node(root.right, data, k=k + 1)

t = Tree(10)
t.root.left = TNode(4)
t.root.left.right = TNode(7)
t.root.left.right.right = TNode(8)
t.root.left.right.right.left = TNode(45)
t.root.right = TNode(20)
t.root.right.left = TNode(70)
t.root.right.left.left = TNode(80)

print "Closet leaf node from the passed node is"
print t.get_closest_leaf_from_a_node(t.root)
print "Height of the closest leaf node from the passed node is"
t.get_height_of_node(t.root, 45, k=0)


