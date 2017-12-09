class Stack(object):
    def __init__(self, initial=[]):
        self.stack = initial

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def get_top(self):
        return self.stack[-1]

    def is_stack_empty(self):
        return True if len(self.stack) == 0 else False

    def print_stack_elements(self):
        for ele in self.stack:
            print ele

s = Stack()
s.pop()
s.push(10)
s.pop()
print s.is_stack_empty()
s.print_stack_elements()