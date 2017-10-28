
class BFS(object):
    def __init__(self, verticies):
        self.graph = dict()
        for vertex in verticies:
            if verticies.count(vertex) >= 2:
                raise Exception("Vertex name can not be duplicate")
            self.graph[vertex] = []
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def bfs_traversal(self):
        pass





bfs = BFS([0, 1,2,3])
print bfs.graph
bfs.add_edge(0, 1)
bfs.add_edge(0, 2)
bfs.add_edge(1, 2)
bfs.add_edge(2, 0)
bfs.add_edge(2, 3)
bfs.add_edge(3, 3)
print bfs.graph

