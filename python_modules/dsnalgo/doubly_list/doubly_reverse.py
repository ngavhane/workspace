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

    def reverse_doubly(self):
        temp = self.head
        xyz = None
        while temp:
            pqr = temp
            temp = temp.next
            pqr.next = xyz
            pqr.prev = None
            if xyz is not None:
                xyz.prev = pqr
            xyz = pqr
        self.head = xyz


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

print "reversing doubly"
d.reverse_doubly()

print "List from head"
d.print_d_list_from_head()
print "List from Last"
d.print_d_list_from_end()

