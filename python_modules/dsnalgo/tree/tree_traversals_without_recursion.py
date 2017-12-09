class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Slist(object):

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data)
            return
        elif self.head.next is None:
            self.head.next = Node(data=data)
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def delete_at_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            ele = self.head.data
            self.head = None
            return ele
        else:
            temp = self.head
            while temp.next:
                temp_succ = temp
                temp = temp.next
            ele = self.head.data
            temp_succ.next = None
            return ele

    def get_last_element(self):
        if self.head is None:
            return
        elif self.head.next is None:
            ele = self.head.data
            return ele
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            ele = temp.data
            return ele

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def is_list_empty(self):
        return True if self.head is None else False


class Stack(object):
    def __init__(self):
        self.stack = Slist()

    def push(self, element):
        self.stack.insert_at_end(element)

    def pop(self):
        return self.stack.delete_at_last()

    def is_stack_empty(self):
        return self.stack.is_list_empty()

    def print_stack(self):
        self.stack.print_list()

    def get_top(self):
        return self.stack.get_last_element()


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

    def inorder_traversal_without_recursion_and_using_stack(self, root):
        already_visited = []
        stack = Stack()
        if root is not None:
            stack.push(root)
        while not stack.is_stack_empty():
            top = stack.get_top()
            if top.left is not None and top.left not in already_visited:
                stack.push(top.left)
            else:
                stack.pop()
                print top.data
                already_visited.append(top)
                if top.right is not None:
                    stack.push(top.right)

    def preorder_traversal_without_recursion_and_using_stack(self, root):
        already_visited = []
        already_printed = []
        stack = Stack()
        if root is not None:
            stack.push(root)
        while not stack.is_stack_empty():
            top = stack.get_top()
            already_visited.append(top)
            if top not in already_printed:
                print top.data
                already_printed.append(top)
            if top.left is not None and top.left not in already_visited:
                stack.push(top.left)
            else:
                stack.pop()
                if top.right is not None and top.right not in already_visited:
                    stack.push(top.right)

    def postorder_traversal_without_recursion_and_using_stack(self, root):
        already_visited = []
        already_printed = []
        stack = Stack()
        if root is not None:
            stack.push(root)
        while not stack.is_stack_empty():
            top = stack.get_top()
            if top not in already_visited:
                already_visited.append(top)
            if top.left is not None and top.left not in already_visited:
                stack.push(top.left)
            else:
                if top.right is not None and top.right not in already_visited:
                    stack.push(top.right)
                else:
                    stack.pop()
                    if top not in already_printed:
                        print top.data
                        already_printed.append(top)


bst = BstTree(10)
bst.insert_node(bst.root, 9)
bst.insert_node(bst.root, 15)
bst.insert_node(bst.root, 7)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, -9)
bst.insert_node(bst.root, 21)
bst.insert_node(bst.root, 1)
print "****** In-order traversal of the tree is"
bst.inorder_traversal_without_recursion_and_using_stack(bst.root)

print "****** Pre-order traversal of the tree is"
bst.preorder_traversal_without_recursion_and_using_stack(bst.root)

print "****** Post-order traversal of the tree is"
bst.postorder_traversal_without_recursion_and_using_stack(bst.root)

