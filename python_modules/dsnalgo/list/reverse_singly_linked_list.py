class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def reverse_list(self):
        temp = self.head
        pqr = None
        while(temp):
            xyz = temp
            temp = temp.next
            xyz.next = pqr
            pqr = xyz
        self.head = pqr

    def get_all_list_elements(self):
        all_ele = []
        temp = self.head
        while(temp):
            all_ele.append(temp.data)
            temp = temp.next
        return all_ele

    def print_li(self):
        temp = self.head
        while(temp):
            print temp.data
            temp= temp.next
s=SList()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)
s.print_li()
print "reverse"
s.reverse_list()
s.print_li()


