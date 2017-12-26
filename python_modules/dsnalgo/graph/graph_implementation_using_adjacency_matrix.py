class Queue(object):
    def __init__(self, initial=[]):
        self.queue = initial

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequque(self):
        if len(self.queue) == 0:
            return
        return self.queue.pop()

    def is_queue_empty(self):
        return True if len(self.queue) == 0 else False

    def print_queue_elements(self):

        print(' '.join(str(x) for x in self.queue))

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
        print "stack lement", (' '.join(str(x) for x in self.stack))


class Graph(object):
    def __init__(self, vertices):
        self.edge_map = [[0 for _ in range(1, vertices+1)] for _ in range(1, vertices+1)]

    def add_edge_to_graph(self, source, destination):
        self.edge_map[source][destination] = 1
        self.edge_map[destination][source] = 1

    def bfs_search(self, start):
        bfs_visited_status = []
        queue = Queue()
        for _ in range(len(self.edge_map)):
            bfs_visited_status.append(False)
        queue.enqueue(start)
        while not queue.is_queue_empty():
            vertex_to_visited = queue.dequque()
            bfs_visited_status[vertex_to_visited] = True
            print vertex_to_visited
            vertex_adj = self.edge_map[vertex_to_visited]
            for index, value in enumerate(vertex_adj):
                if value == 1 and bfs_visited_status[index] is False:
                    if index not in queue.queue:
                        queue.enqueue(index)

    def dfs_search(self, start):
        bfs_visited_status = []
        stack = Stack()
        for _ in range(len(self.edge_map)):
            bfs_visited_status.append(False)
        stack.push(start)
        while not stack.is_stack_empty():
            vertex_to_visited = stack.get_top()
            if not bfs_visited_status[vertex_to_visited]:
                print vertex_to_visited
            bfs_visited_status[vertex_to_visited] = True
            vertex_adj = self.edge_map[vertex_to_visited]
            pop = True
            for index, value in enumerate(vertex_adj):
                if value == 1 and bfs_visited_status[index] is False:
                    pop = False
                    break
            if pop:
               stack.pop()
            for index, value in enumerate(vertex_adj):
                if value == 1 and bfs_visited_status[index] is False:
                    if index not in stack.stack:
                        stack.push(index)
                        break

    def print_matrix(self):
        print self.edge_map
n = 6
g = Graph(n)
g.print_matrix()

g.add_edge_to_graph(0, 1)
g.add_edge_to_graph(1, 3)
g.add_edge_to_graph(1, 4)
g.add_edge_to_graph(2, 4)
g.add_edge_to_graph(3, 5)
g.add_edge_to_graph(4, 5)
g.print_matrix()

print "BFS search on the tree:"
g.bfs_search(start=0)

print "DFS search on the tree:"
g.dfs_search(start=2)

