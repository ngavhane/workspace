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

    def insert_at_beg(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        temp.prev = self.head

    def insert_after_value(self, data, after):
        temp = self.head
        while temp.data != after:
            temp = temp.next

        xyz = temp.next
        temp.next = Node(data)
        temp.next.next = xyz
        temp.next.prev = temp
        xyz.prev = temp.next

    def print_d_list_from_head(self):
        temp = self.head
        while temp.next:
            print temp.data
            print "Next data" + str(temp.next.data)
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
d.insert_at_beg(70)
print "List from head"
#d.print_d_list_from_head()

print "List from Last"
#d.print_d_list_from_end()

d.insert_after_value(90, 40)
print "List from head"
#d.print_d_list_from_head()
print "List from Last"
d.print_d_list_from_end()

