from collections import defaultdict

class Vertex:
    def __init__(self, name):
        self.name = name

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self, num_vertices):
        self.vertices = []
        self.adjacency_list = defaultdict(dict)
        self.num_vertices = num_vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1][vertex2] = weight
        self.adjacency_list[vertex2][vertex1] = weight

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def kruskal(graph):
    edges = []
    for vertex in graph.adjacency_list:
        for neighbor, weight in graph.adjacency_list[vertex].items():
            edges.append(Edge(vertex, neighbor, weight))

    edges.sort(key=lambda x: x.weight)
    uf = UnionFind(len(graph.vertices))
    mst = []

    for edge in edges:
        if uf.find(graph.vertices.index(edge.u)) != uf.find(graph.vertices.index(edge.v)):
            uf.union(graph.vertices.index(edge.u), graph.vertices.index(edge.v))
            mst.append(edge)

    return mst

if __name__ == "__main__":
    # Example from figure 23.4 of Chapter 23 of 2009 Introduction to Algorithms by Cormen et al.
    # 0: a, 1: b, 2: c, 3: d, 4: e, 5: f, 6: g, 7: h, 8: i
    graph = Graph(9)
    a, b, c, d, e, f, g, h, i = Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d'), Vertex('e'), Vertex('f'), Vertex('g'), Vertex('h'), Vertex('i')
    for v in [a, b, c, d, e, f, g, h, i]:
        graph.add_vertex(v)
    graph.add_edge(a, b, 4)
    graph.add_edge(a, h, 8)
    graph.add_edge(b, c, 8)
    graph.add_edge(b, h, 11)
    graph.add_edge(c, d, 7)
    graph.add_edge(c, e, 4)
    graph.add_edge(c, i, 2)
    graph.add_edge(d, e, 9)
    graph.add_edge(d, f, 14)
    graph.add_edge(e, f, 10)
    graph.add_edge(f, g, 2)
    graph.add_edge(g, h, 1)
    graph.add_edge(g, i, 6)
    graph.add_edge(h, i, 7)

    mst = kruskal(graph)
    for edge in mst:
        print(f"{edge.u.name} - {edge.v.name}")