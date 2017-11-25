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

    def swap_nth_node_from_start_with_nth_node_from_end(self, n):
        first = self.head
        last = self.head
        while last.next:
            last = last.next
        while n:
            n = n-1
            first = first.next
            last = last.prev
        temp = first.data
        first.data = last.data
        last.data = temp

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


d.swap_nth_node_from_start_with_nth_node_from_end(n=3)
print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()


