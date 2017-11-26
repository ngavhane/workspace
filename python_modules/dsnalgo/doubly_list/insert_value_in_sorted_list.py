class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyList(object):
    def __init__(self, data):
        self.head = Node(data)

    def insert_at_last(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
        temp.next.prev = temp

    def insert_value_in_sorted_d_list(self, value):
        temp = self.head
        while temp.next.data < value:
            temp = temp.next
            if temp.next is None:
                break
        if temp == self.head:   # the place where new node is to insert is the first one
            self.head = Node(value)
            self.head.next = temp
            temp.prev = self.head
        elif temp.next is None:  # the place where new node is to insert is the last One
            temp.next = Node(value)
            temp.next.prev = temp
        else:
            xyz = temp.next
            temp.next = Node(value)
            temp.next.next = xyz
            temp.next.prev = temp
            xyz.prev = temp.next

    def print_d_list_from_head(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def print_d_list_from_end(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print temp.data
            temp = temp.prev


d = DoublyList(10)
d.insert_at_last(20)
d.insert_at_last(30)
d.insert_at_last(40)
d.insert_at_last(50)
d.insert_at_last(60)

print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()

print "Test if insertion at first node is working"
d.insert_value_in_sorted_d_list(9)
print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()

print "Test if insertion at last node is working"
d.insert_value_in_sorted_d_list(70)
print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()

print "Test if insertion at intermediate node is working"
d.insert_value_in_sorted_d_list(41)
print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()

