class Graph:
    def __init__(self):
        # Dictionary to hold adjacency list: node -> {neighbor: weight, ...}
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1][v2] = weight
        self.adj_list[v2][v1] = weight  # Remove this line for directed graph

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

# graph = {
#     "U": {"V": 6, "W": 7},
#     "V": {"U": 6, "X": 10},
#     "W": {"U": 7, "X": 1},
#     "X": {"W": 1, "V": 10}
# }
graph = Graph()

graph.add_edge('U', 'V', 6)
graph.add_edge('U', 'W', 7)
graph.add_edge('V', 'X', 10)
graph.add_edge('W', 'X', 1)

graph.print_graph()

INF = float("infinity")

vertex_short_distance ={
    'U' : 0,
    'V' : INF,
    'X' : INF,
    'W' : INF
}

visited_vertex = []
unvisited_vertex = ['U','V','X','W']


while len(unvisited_vertex) >0:
    current_vertex = unvisited_vertex.pop(0)
    visited_vertex.append(current_vertex)
    current_neighbour = graph.adj_list.get(current_vertex).items()
    for vertex,vertex_distance in current_neighbour:
        print(f'vertex: {vertex} distance: {vertex_distance}')
        if(vertex_short_distance[vertex]>vertex_distance):
            vertex_short_distance[vertex] = vertex_distance
    print(vertex_short_distance)


#print(unvisited_vertex)