class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Singly_link(object):
    def __init__(self):
        self.head = None

    def insert_at_last(self, data):
        if self.head is None:   # handle scenario where list is empty
            self.head = Node(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def move_last_element_to_first(self):
        temp = self.head
        temp_succ = None
        while temp.next:
            temp_succ = temp
            temp=temp.next
        temp_succ.next = None
        temp_succ = self.head
        self.head = temp
        self.head.next = temp_succ

    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

sl=Singly_link()
sl.insert_at_last(10)
sl.insert_at_last(20)
sl.insert_at_last(30)
sl.insert_at_last(40)
sl.insert_at_last(50)
sl.insert_at_last(60)
sl.print_list()
print "*****"
sl.move_last_element_to_first()
print "***"
sl.print_list()



