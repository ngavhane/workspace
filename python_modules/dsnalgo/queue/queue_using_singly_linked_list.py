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
        if temp.next is None:
            element = temp.data
            self.head = None
        else:
            while temp.next:
                temp_succ = temp
                temp = temp.next
            element = temp.data
            if temp_succ is not None:
                temp_succ.next = None
        return element

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def is_slist_empty(self):
        return True if self.head is None else False

class Queue(object):
    def __init__(self):
        self.slist = SList()

    def enqueue(self, element):
        self.slist.insert_at_beg(element)

    def dequeue(self):
        return self.slist.delete_at_last()

    def print_queue_from_front_to_rear(self):
        self.slist.print_list()

    def is_queue_empty(self):
        return self.slist.is_slist_empty()


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



