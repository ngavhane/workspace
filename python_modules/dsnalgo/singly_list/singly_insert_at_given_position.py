class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Singly_link(object):
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def insert_at_last(self, data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def insert_after_node(self, data, after_node):
        temp = self.head
        while(temp.data !=after_node):
            temp =temp.next
        xyz = temp
        pqr= temp.next
        xyz.next = Node(data)
        xyz.next.next = pqr


    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data
            #print temp
            #print temp.next
            temp = temp.next

sl=Singly_link()
sl.insert_at_begin(10)
sl.insert_at_begin(20)
sl.insert_at_begin(40)
sl.print_list()
print "***"
sl.insert_at_last(30)
sl.print_list()
print "***"
sl.insert_after_node(10, 30)
sl.print_list()
print "***"

