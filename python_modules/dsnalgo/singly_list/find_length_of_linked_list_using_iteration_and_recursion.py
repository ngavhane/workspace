class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Singly_link(object):
    def __init__(self):
        self.head = None

    def insert_at_last(self, data):
        if self.head is None:   # handle scenario where singly_list is empty
            self.head = Node(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def find_length_using_iteration(self):
        temp = self.head
        lenght = 0
        while(temp):
            lenght += 1
            temp = temp.next
        return lenght

    def find_length_using_recursion(self, head):
        if head is not None:
            count = 1 + self.find_length_using_recursion(head=head.next)
            return count
        else:
            return 0


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
print sl.find_length_using_recursion(sl.head)


