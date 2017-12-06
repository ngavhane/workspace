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




s = Stack()
s.print_stack()
s.push(3)
s.print_stack()
print s.is_stack_empty()
s.print_stack()