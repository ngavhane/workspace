# Python program to find the nodes at k distance from root

# A Binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printKDistant(root, k):
    if root is None:
        return
    if k == 0:
        print root.data,
    else:
        printKDistant(root.left, k - 1)
        printKDistant(root.right, k - 1)

def get_level_of_node(root, k, data):
    if root is None:
        pass
    elif root.data == data:
        print k
    else:
        get_level_of_node(root.left, k+1, data=data)
        get_level_of_node(root.right, k + 1, data=data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(10)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.left.left = Node(10)

get_level_of_node(root, 1, 10)