class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SList(object):
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        if self.head is None:
            self.head = Node(data=data)
            return
        temp = self.head
        self.head = Node(data=data)
        self.head.next = temp

    def delete_at_last(self):
        temp_succ = None
        temp = self.head
        while temp.next:
            temp_succ = temp
            temp = temp.next
        if temp_succ.next is not None:
            temp_succ.next = None

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

class Queue(object):
    def __init__(self):
        self.slist = SList()

    def enqueue(self, element):
        self.slist.insert_at_beg(element)

    def dequeue(self):
        self.slist.delete_at_last()

    def print_queue_from_front_to_rear(self):
        self.slist.print_list()


q = Queue()
q.enqueue(10)
q.dequeue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print "*****"
q.print_queue_from_front_to_rear()
q.dequeue()
print "*****"
q.print_queue_from_front_to_rear()
q.dequeue()
print "******"
q.print_queue_from_front_to_rear()
q.enqueue(540)
print "******"
q.print_queue_from_front_to_rear()



