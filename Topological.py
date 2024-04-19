from collections import defaultdict

class Vertex:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)

def topological_sort(graph):
    in_degree = {v: 0 for v in graph.vertices}
    for vertex in graph.adjacency_list:
        for neighbor in graph.adjacency_list[vertex]:
            in_degree[neighbor] += 1

    queue = [v for v in graph.vertices if in_degree[v] == 0]
    sorted_vertices = []

    while queue:
        vertex = queue.pop(0)
        sorted_vertices.append(vertex)

        for neighbor in graph.adjacency_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_vertices) != len(graph.vertices):
        raise ValueError("The graph contains a cycle.")

    return sorted_vertices

if __name__ == "__main__":
    graph = Graph()

    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")
    for v in [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]:
        graph.add_vertex(v)
    graph.add_edge(undershorts, pants)
    graph.add_edge(undershorts, shoes)
    graph.add_edge(pants, shoes)
    graph.add_edge(pants, belt)
    graph.add_edge(shirt, tie)
    graph.add_edge(tie, jacket)
    graph.add_edge(shirt, belt)
    graph.add_edge(belt, jacket)
    graph.add_edge(socks, shoes)

    print([v.name for v in topological_sort(graph)])