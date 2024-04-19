from collections import defaultdict

class Vertex:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self, num_vertices):
        self.vertices = []
        self.adjacency_list = defaultdict(list)
        self.num_vertices = num_vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex.name)
            for neighbor in reversed(graph.adjacency_list[vertex]):
                stack.append(neighbor)

    return result

if __name__ == "__main__":
    # Example from figure 22.4 of Chapter 22 of 2009 Introduction to Algorithms by Cormen et al.
    graph = Graph(6)
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_vertex(u)
    graph.add_vertex(v)
    graph.add_vertex(w)
    graph.add_vertex(x)
    graph.add_vertex(y)
    graph.add_vertex(z)
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    print(dfs(graph, u))  # Output: ['u', 'v', 'y', 'x', 'w', 'z']