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

    def delete_node(self, data):
        """
        Need to Handle three conditions here:
        1. first node
        2. last node
        3. in between node
        """
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        temp = self.head
        while temp.data != data:
            temp_succ = temp
            temp = temp.next
        temp_succ.next = temp.next
        if temp.next:  # handling scenario where the node which is to deleted is last
            temp.next.prev = temp_succ



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


d.delete_node(60)
print "List from head"
d.print_d_list_from_head()

print "List from Last"
d.print_d_list_from_end()


