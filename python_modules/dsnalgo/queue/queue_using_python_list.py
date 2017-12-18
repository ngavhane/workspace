class Queue(object):
    def __init__(self, initial=[]):
        self.queue = initial

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequque(self):
        if len(self.queue) == 0:
            return
        self.queue.pop()

    def is_queue_empty(self):
        return True if len(self.queue) == 0 else False

    def print_queue_elements(self):
        for ele in self.queue:
            print ele

q = Queue()
q.dequque()
print q.is_queue_empty()
q.enqueue(10)
q.dequque()
q.enqueue(20)
q.enqueue(30)
print q.is_queue_empty()
q.print_queue_elements()


